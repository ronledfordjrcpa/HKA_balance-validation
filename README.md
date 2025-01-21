markdown
# Balance Validation Script

## Overview
This repository contains a Python script for validating balances between Dynamics GP (source) and Sage Intacct (target). The script maps GL accounts, compares balances, and generates a report of any discrepancies.

## Installation Instructions

1. **Install Python**
   Ensure Python is installed on your system. Download it from [python.org](https://www.python.org/downloads/).

2. **Install Required Libraries**
   Open Command Prompt and run the following command to install the necessary libraries:
   ```bash
   pip install pandas openpyxl
3. Create the run_validation.bat File Open a text editor and create a new file named run_validation.bat. Add the following commands:

batch
@echo off
REM Copy required files to the working directory
copy path\to\source\dynamics_gp.xlsx .\dynamics_gp.xlsx
copy path\to\source\sage_intacct.xlsx .\sage_intacct.xlsx
copy path\to\source\mapping_file.xlsx .\mapping_file.xlsx

REM Run the Python script
python balance_validation.py
pause
4. Place Your Files Place your Dynamics GP, Sage Intacct, and Mapping Excel files in the specified paths. Update the file paths in balance_validation.py and run_validation.bat accordingly.

How to Use the Script
1. Place your Dynamics GP, Sage Intacct, and Mapping Excel files in the specified paths.

2. Update the file paths in balance_validation.py and run_validation.bat accordingly.

3. Run the script by opening Command Prompt, navigating to the script's directory, and executing:

bash
run_validation.bat
4. The output report (balance_validation_report.xlsx) will be generated in the script’s directory.

Folder Structure
Your project directory should look like this:

balance_validation/
├── balance_validation.py
├── README.md
├── run_validation.bat
├── dynamics_gp.xlsx
├── sage_intacct.xlsx
├── mapping_file.xlsx
└── .gitignore
Contributing
Feel free to fork this repository and submit pull requests. If you encounter any issues, please report them via the issue tracker.

License
This project is licensed under the MIT License - see the LICENSE file for details.

