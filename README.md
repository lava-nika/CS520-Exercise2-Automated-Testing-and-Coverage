# Exercise 2: Automated Testing & Coverage

Course: CS 520 - Fall 2025 <br>
Name: Lavanika Srinivasaraghavan

## Quick Start

### Setup

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

   This installs:
   - `pytest` - Testing framework  
   - `pytest-cov` - Coverage plugin for pytest
   - `coverage` - Core coverage measurement tool

---

## Instructions to run

### Part 1: Run Baseline Coverage

```bash
python run_baseline_coverage.py
```

**Generates:**
- `coverage_results/baseline_coverage_results.json` - Detailed per-solution metrics
- `coverage_results/baseline_coverage_summary.txt` - Summary table

### Part 2: LLM-Assisted Test Generation

```bash
python analyze_iteration.py
```

**Shows:** Baseline → Improved coverage for problem 10 and problem 4

**Generates:**
- `part2_results/iteration_1_results.json` - Coverage improvement metrics and test counts

### Part 3: Fault Detection

```bash
python test_fault_detection.py
```

**Generates:** `part3_workspace/fault_detection_results.json` - Bug detection results


---

## Submission Contents

### Documentation
- **`Exercise2_Final_Report_Lavanika.md` OR `Exercise2_Final_Report_Lavanika.pdf`** - Final report 
- **`README.md`** - This file; setup and execution instructions
- **`requirements.txt`** - Python dependencies (pytest, pytest-cov, coverage)

### Code files
- **`run_baseline_coverage.py`** - Part 1: Analyzes baseline coverage for 180 solutions (2 LLMs x 3 strategies x 3 samples each x 10 problems)
- **`analyze_iteration.py`** - Part 2: Measures coverage improvements with LLM tests
- **`test_fault_detection.py`** - Part 3: Tests bug detection capability of test suites
- **`problem_loader.py`** - Helper to load HumanEval problem definitions
- **`setup_part2.py`** - Setup script that creates Part 2 workspace structure

### Generated Results

#### Part 1 - Baseline Coverage
- **`coverage_results/baseline_coverage_results.json`** - Per-solution coverage metrics (180 solutions)
- **`coverage_results/baseline_coverage_summary.txt`** - Summary table 

#### Part 2 - LLM Test Generation
- **`part2_workspace/problem10/`**
  - `iteration_1_prompt.txt` - Prompt sent to Gemini 2.5 Flash for test generation
  - `iteration_1_response_tests.py` - 7 LLM-generated tests for problem 10
  - `problem_description.txt` - Problem task and baseline tests
- **`part2_workspace/problem4/`**
  - `iteration_1_prompt.txt` - Prompt sent to Gemini 2.5 Flash
  - `iteration_1_response_tests.py` - 7 LLM-generated tests for problem 4
  - `problem_description.txt` - Problem task and baseline tests
- **`part2_results/iteration_1_results.json`** - Coverage improvement metrics and test counts

#### Part 3 - Fault Detection
- **`part3_workspace/problem10/buggy_versions/`**
  - `bug1_off_by_one.py` - Range error (1-8 instead of 1-9)
  - `bug2_wrong_sort.py` - Missing reverse=True
  - `bug3_no_exception_handling.py` - No try-except block
  - `bug4_wrong_boundary.py` - Dictionary includes 0 (should start at 1)
- **`part3_workspace/problem4/buggy_versions/`**
  - `bug1_off_by_one.py` - Incorrect loop initialization
  - `bug2_missing_empty_check.py` - Wrong slice indexing
  - `bug3_no_reversal.py` - Missing string reversal
  - `bug4_broken_helper.py` - Broken is_palindrome function
- **`part3_workspace/fault_detection_results.json`** - Bug detection analysis

### Exercise 1 Reference Code
- **`Ex1/selected_humaneval_problems.json`** - 10 HumanEval problems
- **`Ex1/generated code/`** - 180 solution files (90 Claude + 90 GPT-5)
- **`Ex1/prompts/`** - Exercise 1 prompts for reference

---
