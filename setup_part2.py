#!/usr/bin/env python3

import json
from pathlib import Path
from problem_loader import load_humaneval_problems

SELECTED_PROBLEMS = {
    "problem10": "by_length - 78.1% branch coverage, 20-line solution with try-except and dict operations",
    "problem4": "make_palindrome - 83.1% branch coverage, algorithm with while loop and helper function"
}

def main():
    problems = load_humaneval_problems()
    
    print("\nSelected problems for Part 2:")
    for i, (problem_id, description) in enumerate(SELECTED_PROBLEMS.items(), 1):
        print(f"{i}. {problem_id}: {description}")
    
    workspace = Path(__file__).parent / "part2_workspace"
    workspace.mkdir(exist_ok=True)
    
    for problem_id in SELECTED_PROBLEMS.keys():
        problem_dir = workspace / problem_id
        problem_dir.mkdir(exist_ok=True)
        
        problem_data = problems[problem_id]
        
        with open(problem_dir / "problem_description.txt", 'w') as f:
            f.write(f"Problem: {problem_id}\n")
            f.write(f"Function: {problem_data['entry_point']}\n")
            f.write("="*80 + "\n\n")
            f.write("TASK:\n")
            f.write(problem_data['prompt'])
            f.write("\n\n")
            f.write("TESTS:\n")
            f.write(problem_data['test'])
        
        print(f"\n Created workspace for {problem_id}")
        print(f"  Location: {problem_dir}")


if __name__ == "__main__":
    main()
