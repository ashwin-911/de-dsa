# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Purpose

DSA practice problems focused on Data Engineering interviews, following **Striver's SDE Sheet** as the problem source. All solutions are in Python.

## Running Solutions

Each file is a standalone Python script with a `__main__` block:

```bash
python arrays/2_sum.py
python arrays/set_matrix_zero.py
```

No build system, package manager, or test framework is used.

## File Structure Convention

Every solution file follows this exact pattern:

1. **Top-level docstring** — problem statement, conceptual logic per approach, and complexity analysis for all approaches
2. **Approach functions** — ordered from Brute Force → Better → Optimal, each with its own docstring (Visual Intuition, Steps, Complexity)
3. **Driver code** — `if __name__ == "__main__":` block with test cases demonstrating all approaches

### Naming conventions
- Functions: `problemName_Brute`, `problemName_Better`, `problemName_Optimal` (or `_Hashing`, `_TwoPointers`, etc. for specificity)
- Files: `snake_case.py` (e.g., `longest_subarray_with_sum_k.py`)
- Files with uppercase exist for some problems (e.g., `Maximum_Subarray_Sum.py`) — follow the existing file's casing when editing

## Problem Organization

Currently only an `arrays/` directory exists. Future topics (strings, linked lists, trees, etc.) should each get their own directory at the repo root.

One misplaced file exists at the root: `remove_duolicates_from_sorted_array.py` (note the typo in the filename) — this belongs in `arrays/`.
