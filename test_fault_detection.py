#!/usr/bin/env python3
# Part 3: Fault Detection Check

import json
import sys
import importlib.util
from pathlib import Path
from typing import Dict, List, Tuple
import tempfile
import shutil

with open('selected_humaneval_problems.json', 'r') as f:
    problems_data = json.load(f)

PROBLEM_MAPPING = {
    'problem10': 'HumanEval/105',
    'problem4': 'HumanEval/10'
}


def load_module_from_file(file_path: str, module_name: str):
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    return module


def run_tests_on_buggy_version(problem_id: str, bug_file: Path, test_type: str) -> Tuple[bool, List[str]]:
    task_id = PROBLEM_MAPPING[problem_id]
    problem_data = problems_data[task_id]
    entry_point = problem_data['entry_point']
    
    try:
        buggy_module = load_module_from_file(str(bug_file), f"buggy_{problem_id}_{bug_file.stem}")
        buggy_function = getattr(buggy_module, entry_point)
    except Exception as e:
        return False, [f"Failed to load buggy module: {str(e)}"]
    
    failed_tests = []
    
    if test_type == "baseline":
        test_code = problem_data['test']
        
        test_globals = {entry_point: buggy_function}
        
        try:
            exec(test_code, test_globals)
            check_func = test_globals['check']
            check_func(buggy_function)
            return True, []
        except AssertionError as e:
            return False, ["HumanEval baseline test"]
        except Exception as e:
            return False, [f"HumanEval baseline test (exception: {type(e).__name__})"]
    
    elif test_type == "improved":
        llm_test_file = Path(f"part2_workspace/{problem_id}/iteration_1_response_tests.py")
        
        if not llm_test_file.exists():
            return False, ["LLM test file not found"]
        
        try:
            mock_solution = type(sys)('solution')
            setattr(mock_solution, entry_point, buggy_function)
            sys.modules['solution'] = mock_solution
            
            llm_tests_module = load_module_from_file(
                str(llm_test_file),
                f"llm_tests_{problem_id}_{bug_file.stem}"
            )
            
            test_functions = [
                getattr(llm_tests_module, name) 
                for name in dir(llm_tests_module) 
                if name.startswith('test_')
            ]
            
            for test_func in test_functions:
                try:
                    test_func()
                except AssertionError as e:
                    failed_tests.append(test_func.__name__)
                except Exception as e:
                    failed_tests.append(f"{test_func.__name__} (exception: {type(e).__name__})")
            
            test_code = problem_data['test']
            test_globals = {entry_point: buggy_function}
            
            try:
                exec(test_code, test_globals)
                check_func = test_globals['check']
                check_func(buggy_function)
            except (AssertionError, Exception) as e:
                failed_tests.append("HumanEval baseline")
            
            return len(failed_tests) == 0, failed_tests
            
        except Exception as e:
            return False, [f"Error running improved tests: {str(e)}"]
        finally:
            if 'solution' in sys.modules:
                del sys.modules['solution']
    
    return False, ["Unknown test type"]


def analyze_fault_detection():
    results = {}
    
    for problem_id in ['problem10', 'problem4']:
        print(f"\n{'='*70}")
        print(f"Analyzing {problem_id}")
        print(f"{'='*70}")
        
        bug_dir = Path(f"part3_workspace/{problem_id}/buggy_versions")
        bug_files = sorted(bug_dir.glob("bug*.py"))
        
        problem_results = {
            'bugs': []
        }
        
        for bug_file in bug_files:
            bug_name = bug_file.stem
            print(f"\n{bug_name}: {bug_file.name}")
            
            with open(bug_file, 'r') as f:
                lines = f.readlines()
                description = []
                for line in lines[:10]:
                    if line.strip().startswith('"""') or line.strip().startswith('Bug'):
                        description.append(line.strip().strip('"'))
                bug_description = ' '.join(description)
            
            print(f"  Description: {bug_description[:100]}...")
            
            baseline_passed, baseline_failed = run_tests_on_buggy_version(
                problem_id, bug_file, "baseline"
            )
            
            improved_passed, improved_failed = run_tests_on_buggy_version(
                problem_id, bug_file, "improved"
            )
            
            baseline_caught = not baseline_passed
            improved_caught = not improved_passed
            
            print(f"  Baseline tests: {'CAUGHT' if baseline_caught else 'MISSED'}")
            if baseline_failed:
                print(f"    Failed tests: {', '.join(baseline_failed[:3])}")
            
            print(f"  Improved tests: {'CAUGHT' if improved_caught else 'MISSED'}")
            if improved_failed:
                print(f"    Failed tests: {', '.join(improved_failed[:3])}")
            
            bug_result = {
                'bug_name': bug_name,
                'description': bug_description,
                'baseline_caught': baseline_caught,
                'baseline_failed_tests': baseline_failed,
                'improved_caught': improved_caught,
                'improved_failed_tests': improved_failed,
                'only_improved_caught': improved_caught and not baseline_caught
            }
            
            problem_results['bugs'].append(bug_result)
        
        total_bugs = len(problem_results['bugs'])
        baseline_caught_count = sum(1 for b in problem_results['bugs'] if b['baseline_caught'])
        improved_caught_count = sum(1 for b in problem_results['bugs'] if b['improved_caught'])
        only_improved_count = sum(1 for b in problem_results['bugs'] if b['only_improved_caught'])
        
        problem_results['summary'] = {
            'total_bugs': total_bugs,
            'baseline_caught': baseline_caught_count,
            'improved_caught': improved_caught_count,
            'only_improved_caught': only_improved_count,
            'baseline_detection_rate': baseline_caught_count / total_bugs if total_bugs > 0 else 0,
            'improved_detection_rate': improved_caught_count / total_bugs if total_bugs > 0 else 0
        }
        
        print(f"\n{problem_id} Summary:")
        print(f"  Total bugs: {total_bugs}")
        print(f"  Baseline caught: {baseline_caught_count}/{total_bugs} ({problem_results['summary']['baseline_detection_rate']*100:.1f}%)")
        print(f"  Improved caught: {improved_caught_count}/{total_bugs} ({problem_results['summary']['improved_detection_rate']*100:.1f}%)")
        print(f"  Only improved caught: {only_improved_count}")
        
        results[problem_id] = problem_results
    
    print(f"\n{'='*70}")
    print("OVERALL SUMMARY")
    print(f"{'='*70}")
    
    total_bugs = sum(r['summary']['total_bugs'] for r in results.values())
    total_baseline_caught = sum(r['summary']['baseline_caught'] for r in results.values())
    total_improved_caught = sum(r['summary']['improved_caught'] for r in results.values())
    total_only_improved = sum(r['summary']['only_improved_caught'] for r in results.values())
    
    print(f"Total bugs seeded: {total_bugs}")
    print(f"Baseline detection rate: {total_baseline_caught}/{total_bugs} ({total_baseline_caught/total_bugs*100:.1f}%)")
    print(f"Improved detection rate: {total_improved_caught}/{total_bugs} ({total_improved_caught/total_bugs*100:.1f}%)")
    print(f"Bugs caught ONLY by improved tests: {total_only_improved}")
    
    with open('part3_workspace/fault_detection_results.json', 'w') as f:
        json.dump(results, f, indent=2)
    
    print(f"\nResults saved to part3_workspace/fault_detection_results.json")
    
    return results


if __name__ == "__main__":
    analyze_fault_detection()
