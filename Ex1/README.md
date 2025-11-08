# Exercise 1

**Course**: CS 520 - Fall 2025  
**Name**: Lavanika Srinivasaraghavan

## Submission contents

### Main Report
- **`Final_Report_Lavanika.pdf`** - final report 

### Code & Scripts
- **`evaluate_pass_at_k.py`** - Main evaluation (for all 3 strategies)
- **`analyze_tds_results.py`** - Comparative analysis script for TDS evaluation
- **`generate_tds_prompts.py`** - Automated TDS prompt generator
- **`load_problems.py`** - HumanEval problem loader

### Data & Results
- **`selected_humaneval_problems.json`** - 10 HumanEval problems used in evaluation
- **`prompts/`** - 30 prompt files (10 problems × 3 strategies: CoT, Self-Debug, TDS)
- **`generated code/`** - 180 solutions (60 per strategy, 3 samples per problem, 2 models)
  - `claude sonnet4.5/` - 90 Claude solutions
  - `gpt5/` - 90 GPT-5 solutions
- **`evaluation_results/`** - All evaluation outputs
  - `detailed_results.json` - Per-solution test results
  - `pass_at_k_results.json` - Pass@k metrics for all strategies
  - `evaluation_report.txt` - Human-readable evaluation report
  - `pass_at_k_summary.csv` - Summary table

## Quick Start

### Run Complete Evaluation
```bash
python evaluate_pass_at_k.py
```

### Run TDS Comparative Analysis
```bash
python analyze_tds_results.py
```

### View Results
```bash
# Main report
open Final_Report_Lavanika.pdf 
# OR
open Final_Report_Lavanika.md

# Detailed results
cat evaluation_results/evaluation_report.txt
```
