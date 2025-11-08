# Test Coverage Script for Exercise 2 Part 1: Baseline Coverage
# Runs HumanEval tests against generated solutions with coverage measurement

import json
import os
import sys
import importlib.util
import subprocess
from pathlib import Path
from typing import Dict, List, Tuple
import tempfile
import shutil

EX1_DIR = Path(__file__).parent / "Ex1"
sys.path.insert(0, str(EX1_DIR))


def load_humaneval_problems(json_path: str) -> Dict:
    with open(json_path, 'r') as f:
        return json.load(f)


def get_solution_files(base_dir: Path) -> Dict[str, List[Path]]:
    solutions = {}
    
    # Handle directory names with spaces
    model_dirs = []
    for item in base_dir.iterdir():
        if item.is_dir() and item.name != "fixed_solutions":
            model_dirs.append(item)
    
    for model_dir in model_dirs:
        for problem_dir in model_dir.iterdir():
            if problem_dir.is_dir() and problem_dir.name.startswith("problem"):
                problem_num = problem_dir.name
                
                if problem_num not in solutions:
                    solutions[problem_num] = []
                
                for solution_file in problem_dir.iterdir():
                    if solution_file.is_file() and solution_file.suffix == ".py" and not solution_file.name.endswith("_FIXED.py"):
                        solutions[problem_num].append(solution_file)
    
    return solutions


def run_coverage_for_solution(solution_path: Path, problem_data: Dict) -> Dict:
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_path = Path(temp_dir)
        
        solution_copy = temp_path / solution_path.name
        shutil.copy(solution_path, solution_copy)
        
        test_script = temp_path / "run_test.py"
        test_content = f"""
import sys
sys.path.insert(0, '{temp_path}')

# Import the solution
from {solution_copy.stem} import {problem_data['entry_point']}

# HumanEval test code
{problem_data['test']}

# Run the test
try:
    check({problem_data['entry_point']})
    print("TEST_PASSED")
except Exception as e:
    print(f"TEST_FAILED: {{e}}")
    sys.exit(1)
"""
        with open(test_script, 'w') as f:
            f.write(test_content)
        
        coverage_data_file = temp_path / ".coverage"
        cmd = [
            "coverage", "run",
            "--source", str(temp_path),
            "--data-file", str(coverage_data_file),
            "--branch",
            str(test_script)
        ]
        
        result = subprocess.run(
            cmd,
            cwd=temp_dir,
            capture_output=True,
            text=True
        )
        
        test_passed = "TEST_PASSED" in result.stdout and result.returncode == 0
        
        coverage_data = {
            "solution": solution_path.name,
            "test_passed": test_passed,
            "line_coverage": 0.0,
            "branch_coverage": 0.0,
            "lines_covered": 0,
            "lines_total": 0,
            "branches_covered": 0,
            "branches_total": 0,
            "missing_lines": [],
            "stdout": result.stdout,
            "stderr": result.stderr
        }
        
        json_cmd = [
            "coverage", "json",
            "--data-file", str(coverage_data_file),
            "-o", str(temp_path / "coverage.json")
        ]
        subprocess.run(json_cmd, cwd=temp_dir, capture_output=True)
        
        json_report = temp_path / "coverage.json"
        if json_report.exists():
            try:
                with open(json_report, 'r') as f:
                    cov_data = json.load(f)
                
                for file_path, file_data in cov_data['files'].items():
                    if solution_path.name in file_path:
                        summary = file_data['summary']
                        coverage_data['line_coverage'] = summary['percent_covered']
                        coverage_data['lines_covered'] = summary['covered_lines']
                        coverage_data['lines_total'] = summary['num_statements']
                        coverage_data['missing_lines'] = file_data.get('missing_lines', [])
                        
                        if 'num_branches' in summary and summary['num_branches'] > 0:
                            coverage_data['branches_total'] = summary['num_branches']
                            coverage_data['branches_covered'] = summary['covered_branches']
                            coverage_data['branch_coverage'] = (
                                summary['covered_branches'] / summary['num_branches'] * 100
                            )
                        break
            except Exception as e:
                coverage_data['stderr'] += f"\nError reading coverage: {e}"
        
        return coverage_data


def analyze_coverage_for_problem(problem_num: str, solutions: List[Path], 
                                 problem_data: Dict) -> Dict:
    
    print(f"\n{'='*80}")
    print(f"Analyzing Problem {problem_num}")
    print(f"{'='*80}")
    
    results = []
    
    for solution_path in solutions:
        print(f"\nTesting: {solution_path.name}")
        coverage_data = run_coverage_for_solution(solution_path, problem_data)
        results.append(coverage_data)
        
        status = "PASSED" if coverage_data['test_passed'] else "FAILED"
        print(f"  Status: {status}")
        print(f"  Line Coverage: {coverage_data['line_coverage']:.1f}%")
        print(f"  Lines: {coverage_data['lines_covered']}/{coverage_data['lines_total']}")
        if coverage_data['branches_total'] > 0:
            print(f"  Branch Coverage: {coverage_data['branch_coverage']:.1f}%")
            print(f"  Branches: {coverage_data['branches_covered']}/{coverage_data['branches_total']}")
    
    passed_results = [r for r in results if r['test_passed']]
    passed_count = len(passed_results)
    
    avg_line_coverage = 0.0
    if passed_count > 0:
        avg_line_coverage = sum(r['line_coverage'] for r in passed_results) / passed_count
    
    avg_branch_coverage = 0.0
    branch_results = [r for r in passed_results if r['branches_total'] > 0]
    if branch_results:
        avg_branch_coverage = sum(r['branch_coverage'] for r in branch_results) / len(branch_results)
    
    interpretation = generate_interpretation(avg_line_coverage, avg_branch_coverage, passed_count, len(results))
    
    summary = {
        "problem": problem_num,
        "total_solutions": len(results),
        "passed_solutions": passed_count,
        "failed_solutions": len(results) - passed_count,
        "avg_line_coverage": avg_line_coverage,
        "avg_branch_coverage": avg_branch_coverage,
        "interpretation": interpretation,
        "detailed_results": results
    }
    
    return summary


def generate_interpretation(line_cov: float, branch_cov: float, passed: int, total: int) -> str:
    
    interpretations = []
    
    if passed < total:
        interpretations.append(f"{total - passed} solution(s) failed tests")
    else:
        interpretations.append("All solutions passed tests")
    
    if line_cov >= 90:
        interpretations.append("excellent line coverage")
    elif line_cov >= 75:
        interpretations.append("good line coverage")
    elif line_cov >= 60:
        interpretations.append("moderate line coverage")
    else:
        interpretations.append("low line coverage - may have untested code paths")
    
    if branch_cov > 0:
        if branch_cov >= 80:
            interpretations.append("strong branch coverage")
        elif branch_cov >= 60:
            interpretations.append("moderate branch coverage")
        else:
            interpretations.append("low branch coverage - conditional logic may not be fully tested")
    
    return "; ".join(interpretations)


def create_summary_table(all_results: List[Dict]) -> str:
    
    header = f"{'Problem':<12} {'Tests':<8} {'Passed':<8} {'Line %':<10} {'Branch %':<12} {'Interpretation':<50}"
    separator = "=" * 120
    
    lines = [separator, header, separator]
    
    for result in all_results:
        problem = result['problem']
        tests = f"{result['passed_solutions']}/{result['total_solutions']}"
        passed = "✓" if result['failed_solutions'] == 0 else f"{result['failed_solutions']} ✗"
        line_cov = f"{result['avg_line_coverage']:.1f}%"
        branch_cov = f"{result['avg_branch_coverage']:.1f}%" if result['avg_branch_coverage'] > 0 else "N/A"
        interpretation = result['interpretation'][:48] + "..." if len(result['interpretation']) > 50 else result['interpretation']
        
        line = f"{problem:<12} {tests:<8} {passed:<8} {line_cov:<10} {branch_cov:<12} {interpretation:<50}"
        lines.append(line)
    
    lines.append(separator)
    
    total_solutions = sum(r['total_solutions'] for r in all_results)
    total_passed = sum(r['passed_solutions'] for r in all_results)
    overall_line_cov = sum(r['avg_line_coverage'] * r['passed_solutions'] for r in all_results) / max(total_passed, 1)
    
    branch_results = [(r['avg_branch_coverage'], r['passed_solutions']) for r in all_results if r['avg_branch_coverage'] > 0]
    overall_branch_cov = 0.0
    if branch_results:
        overall_branch_cov = sum(cov * count for cov, count in branch_results) / sum(count for _, count in branch_results)
    
    lines.append(f"\nOverall Statistics:")
    lines.append(f"  Total Solutions Tested: {total_solutions}")
    lines.append(f"  Solutions Passed: {total_passed} ({total_passed/total_solutions*100:.1f}%)")
    lines.append(f"  Solutions Failed: {total_solutions - total_passed}")
    lines.append(f"  Average Line Coverage: {overall_line_cov:.1f}%")
    if overall_branch_cov > 0:
        lines.append(f"  Average Branch Coverage: {overall_branch_cov:.1f}%")
    
    return "\n".join(lines)


def main():
    
    base_dir = EX1_DIR / "generated code"
    problems_json = EX1_DIR / "selected_humaneval_problems.json"
    output_dir = Path(__file__).parent / "coverage_results"
    output_dir.mkdir(exist_ok=True)
    
    print("Loading HumanEval problems...")
    problems = load_humaneval_problems(problems_json)
    
    print("Discovering solution files...")
    solutions_by_problem = get_solution_files(base_dir)
    
    print(f"\nFound solutions for {len(solutions_by_problem)} problems")
    for problem, solutions in sorted(solutions_by_problem.items()):
        print(f"  {problem}: {len(solutions)} solutions")
    
    all_results = []
    
    problem_mapping = {
        "problem1": "HumanEval/0",
        "problem2": "HumanEval/1",
        "problem3": "HumanEval/31",
        "problem4": "HumanEval/10",
        "problem5": "HumanEval/54",
        "problem6": "HumanEval/61",
        "problem7": "HumanEval/108",
        "problem8": "HumanEval/32",
        "problem9": "HumanEval/105",
        "problem10": "HumanEval/163"
    }
    
    for problem_num in sorted(solutions_by_problem.keys()):
        if problem_num in problem_mapping:
            task_id = problem_mapping[problem_num]
            problem_data = problems[task_id]
            solutions = solutions_by_problem[problem_num]
            
            result = analyze_coverage_for_problem(problem_num, solutions, problem_data)
            all_results.append(result)
    
    print(f"\n\n{'='*120}")
    print("Baseline Coverage Summary")
    print(f"{'='*120}\n")
    
    summary_table = create_summary_table(all_results)
    print(summary_table)
    
    results_file = output_dir / "baseline_coverage_results.json"
    with open(results_file, 'w') as f:
        json.dump(all_results, f, indent=2)
    print(f"\n\nDetailed results saved to: {results_file}")
    
    summary_file = output_dir / "baseline_coverage_summary.txt"
    with open(summary_file, 'w') as f:
        f.write(summary_table)
    print(f"Summary table saved to: {summary_file}")
    
    print("\n" + "="*120)
    print("Coverage analysis complete!")
    print("="*120)


if __name__ == "__main__":
    main()
