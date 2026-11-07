# Employee Data Analysis Tool

A command-line Python program that loads employee data from a CSV file and lets you search it, run calculations on it, and combine filters to answer more specific questions. Built with pandas.

## Features

| Option | What it does |
|--------|--------------|
| **1. Search a category** | Find employees by employee ID, name, location, manager or department. Input is validated, and you can search again without restarting. |
| **2. Calculations** | Mean, maximum and minimum of `salary` or `performance_score`, plus a range search that returns every employee between two values. |
| **3. Show the whole table** | Prints the full CSV with nothing truncated. |
| **4. Advanced filtering** | Combine up to 5 categories at once (for example department + location + salary range). Each filter narrows the results, so only employees matching all of them are shown. |

## How to run

1. Install Python 3 and the required libraries:
   ```
   pip install pandas matplotlib
   ```
2. Put `practice_data.csv` in the same folder as `data_analysis.py`.
3. Run the program:
   ```
   python data_analysis.py
   ```
4. Pick an option from the menu and follow the prompts.

## Sample data

The CSV contains sample (not real) employee records with columns such as `employee_id`, `name`, `location`, `manager`, `department`, `salary` and `performance_score`.

## How advanced filtering works

1. You choose up to 5 categories, or type `none` to stop.
2. For each category, text columns (like department) ask for one value, and number columns (like salary) ask for a minimum and maximum.
3. Each filter is applied to the result of the previous one, so the table shrinks step by step.
4. The final table shows only the employees who match every filter.

## What I learned

- Validating user input with `try`/`except` and `while` loops so the program doesn't crash on bad input
- Filtering and summarising data with pandas (`.loc`, `.between()`, `.mean()`, `.max()`, `.min()`)
- Splitting repeated code into reusable functions
- Testing by running the program and comparing the output against a trace table of expected results, which helped me find and fix bugs (for example, max and min being labelled as "mean", and the wrong variable being rounded)

## Possible improvements

- Add automated tests
- Split the code into separate files for searching, calculations and filtering
- Let the user save filtered results to a new CSV file

