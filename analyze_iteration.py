#!/usr/bin/env python3
# process LLM responses and measure coverage improvements

import json
import subprocess
import tempfile
from pathlib import Path
from typing import Dict, Tuple

from problem_loader import load_humaneval_problems


def get_reference_solution(problem_id: str, problem_data: Dict) -> str:
    entry_point = problem_data['entry_point']
    canonical = problem_data['canonical_solution']
    prompt = problem_data['prompt']
    
    if f"def {entry_point}(" in prompt:
        lines = prompt.strip().split('\n')
        preamble_lines = []
        found_entry_point = False
        in_docstring = False
        docstring_closed = False
        
        for line in lines:
            preamble_lines.append(line)
            
            if f"def {entry_point}(" in line:
                found_entry_point = True
                in_docstring = False
                docstring_closed = False
            
            if found_entry_point:
                if '"""' in line or "'''" in line:
                    if not in_docstring:
                        in_docstring = True
                        if line.count('"""') == 2 or line.count("'''") == 2:
                            docstring_closed = True
                            break
                    else:
                        docstring_closed = True
                        break
        
        preamble = '\n'.join(preamble_lines)
        solution = f"{preamble}\n{canonical}\n"
        return solution
    else:
        return f"{prompt}\n{canonical}\n"


def run_coverage_with_tests(problem_id: str, problem_data: Dict, 
                            llm_tests_file: Path) -> Tuple[float, float, bool]:
    
    reference_solution = get_reference_solution(problem_id, problem_data)
    if not reference_solution:
        print(f"ERROR: No reference solution found for {problem_id}")
        return 0.0, 0.0, False
    
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_path = Path(temp_dir)
        
        solution_file = temp_path / "solution.py"
        with open(solution_file, 'w') as f:
            f.write(reference_solution)
        
        test_file = temp_path / "test_solution.py"
        
        with open(llm_tests_file, 'r') as f:
            llm_tests = f.read()
        
        test_content = f"""
import pytest
from solution import {problem_data['entry_point']}

# Original HumanEval tests
def test_original_humaneval():
    \"\"\"Original HumanEval test suite\"\"\"
{problem_data['test']}
check({problem_data['entry_point']})

# LLM-generated tests
{llm_tests.replace('import pytest', '').replace(f'from solution import {problem_data["entry_point"]}', '')}
"""
        
        with open(test_file, 'w') as f:
            f.write(test_content)
        
        coverage_data_file = temp_path / ".coverage"
        
        try:
            result = subprocess.run(
                [
                    "coverage", "run",
                    "--source", str(temp_path),
                    "--data-file", str(coverage_data_file),
                    "--branch",
                    "-m", "pytest", str(test_file), "-v", "--tb=short"
                ],
                cwd=temp_dir,
                capture_output=True,
                text=True,
                timeout=30
            )
            
            tests_passed = result.returncode == 0
            
            json_file = temp_path / "coverage.json"
            subprocess.run(
                ["coverage", "json", "-o", str(json_file), "--data-file", str(coverage_data_file)],
                cwd=temp_dir,
                capture_output=True
            )
            
            if json_file.exists():
                with open(json_file, 'r') as f:
                    cov_data = json.load(f)
                
                for file_path, file_data in cov_data['files'].items():
                    if 'solution.py' in file_path:
                        line_cov = file_data['summary']['percent_covered']
                        
                        branches_covered = file_data['summary'].get('covered_branches', 0)
                        branches_total = file_data['summary'].get('num_branches', 0)
                        
                        if branches_total > 0:
                            branch_cov = (branches_covered / branches_total) * 100
                        else:
                            branch_cov = 100.0 if line_cov == 100.0 else line_cov
                        
                        return line_cov, branch_cov, tests_passed
            
            return 0.0, 0.0, tests_passed
            
        except subprocess.TimeoutExpired:
            print(f"Timeout running tests for {problem_id}")
            return 0.0, 0.0, False
        except Exception as e:
            print(f"Error running coverage for {problem_id}: {e}")
            return 0.0, 0.0, False


def analyze_iteration_1():
    
    print("="*80)
    print("ITERATION 1 RESULTS")
    print("="*80)
    
    problems = load_humaneval_problems()
    results = {}
    
    for problem_id in ["problem10", "problem4"]:
        print(f"\n{'='*80}")
        print(f"Analyzing {problem_id}")
        print(f"{'='*80}")
        
        problem_data = problems[problem_id]
        llm_tests_file = Path(__file__).parent / "part2_workspace" / problem_id / "iteration_1_response_tests.py"
        
        if not llm_tests_file.exists():
            print(f"ERROR: No LLM tests file found at {llm_tests_file}")
            continue
        
        with open(llm_tests_file, 'r') as f:
            content = f.read()
            num_tests = content.count('def test_')
        
        print(f"LLM generated {num_tests} test functions")
        
        baseline_file = Path(__file__).parent / "coverage_results" / "baseline_coverage_results.json"
        with open(baseline_file, 'r') as f:
            baseline_data = json.load(f)
        
        problem_summary = next((r for r in baseline_data if r['problem'] == problem_id), None)
        if not problem_summary:
            print(f"ERROR: No baseline data for {problem_id}")
            continue
        
        baseline_line = problem_summary['avg_line_coverage']
        baseline_branch = problem_summary['avg_branch_coverage']
        
        print(f"Baseline: Line={baseline_line:.1f}%, Branch={baseline_branch:.1f}%")
        
        print("Running coverage with new tests...")
        line_cov, branch_cov, tests_passed = run_coverage_with_tests(problem_id, problem_data, llm_tests_file)
        
        print(f"\nIteration 1 Results:")
        print(f"  Line Coverage:   {baseline_line:.1f}% -> {line_cov:.1f}% (Δ {line_cov - baseline_line:+.1f}%)")
        print(f"  Branch Coverage: {baseline_branch:.1f}% -> {branch_cov:.1f}% (Δ {branch_cov - baseline_branch:+.1f}%)")
        print(f"  Tests Passed:    {tests_passed}")
        print(f"  Tests Generated: {num_tests}")
        
        results[problem_id] = {
            'baseline_line': baseline_line,
            'baseline_branch': baseline_branch,
            'iteration_1_line': line_cov,
            'iteration_1_branch': branch_cov,
            'line_improvement': line_cov - baseline_line,
            'branch_improvement': branch_cov - baseline_branch,
            'tests_generated': num_tests,
            'tests_passed': tests_passed
        }
    
    results_dir = Path(__file__).parent / "part2_results"
    results_dir.mkdir(exist_ok=True)
    
    with open(results_dir / "iteration_1_results.json", 'w') as f:
        json.dump(results, f, indent=2)
    
    print(f"\n{'='*80}")
    print("SUMMARY")
    print(f"{'='*80}")
    
    for problem_id, data in results.items():
        print(f"\n{problem_id}:")
        print(f"  Branch coverage: {data['baseline_branch']:.1f}% -> {data['iteration_1_branch']:.1f}% (Δ {data['branch_improvement']:+.1f}%)")
        print(f"  Tests: {data['tests_generated']} new tests, all passed: {data['tests_passed']}")
    
    print(f"\n{'='*80}")
    print("Next Steps:")
    print(f"{'='*80}")
    
    for problem_id, data in results.items():
        if data['branch_improvement'] < 3.0:
            print(f"\n{problem_id}: Small improvement ({data['branch_improvement']:.1f}%), may be converging")
        else:
            print(f"\n{problem_id}: Good improvement ({data['branch_improvement']:.1f}%), continue with iteration 2")


if __name__ == "__main__":
    analyze_iteration_1()
