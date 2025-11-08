#!/usr/bin/env python3
# functions for loading HumanEval problems

import json
from pathlib import Path
from typing import Dict

def load_humaneval_problems() -> Dict:
    ex1_path = Path(__file__).parent.parent / "Ex1" / "selected_humaneval_problems.json"
    
    if not ex1_path.exists():
        raise FileNotFoundError(f"Cannot find problems file at {ex1_path}")
    
    with open(ex1_path, 'r') as f:
        all_problems = json.load(f)
    
    task_id_to_problem_id = {
        'HumanEval/0': 'problem1',
        'HumanEval/1': 'problem2',
        'HumanEval/10': 'problem4',
        'HumanEval/31': 'problem6',
        'HumanEval/32': 'problem7',
        'HumanEval/54': 'problem8',
        'HumanEval/61': 'problem9',
        'HumanEval/105': 'problem10',
        'HumanEval/108': 'problem3',
        'HumanEval/163': 'problem5'
    }
    
    problems = {}
    for task_id, problem_id in task_id_to_problem_id.items():
        if task_id in all_problems:
            problems[problem_id] = all_problems[task_id]
    
    return problems


def get_problem_by_id(problem_id: str) -> Dict:
    problems = load_humaneval_problems()
    return problems.get(problem_id)


if __name__ == "__main__":
    problems = load_humaneval_problems()
    print(f"Loaded {len(problems)} problems:")
    for problem_id, data in problems.items():
        print(f"  {problem_id}: {data['entry_point']}")
