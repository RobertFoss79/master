# Budgeting App
#### Video Demo:  <URL HERE>
#### Description:
This project is a basic budgeting application that allows users to enter their income and expenses, save this data to a file, and load it when needed. The application is implemented in Python and is designed to be user-friendly with interactive prompts.

## Files
- `project.py`: Main program file containing the main function and additional required functions.
- `income.py`: Contains functions for inputting income.
- `expenses.py`: Contains functions for inputting expenses.
- `utils.py`: Utility functions for saving and loading data.
- `test_project.py`: Contains tests for the functions in `project.py`.
- `requirements.txt`: Lists the required pip-installable libraries for the project.

## Usage
1. Run `project.py` to start the budgeting application.
2. Follow the prompts to enter income and expenses.
3. Save the data to a specified file.
4. Load existing data by providing the file path.

## Design Choices
- The application uses a simple command-line interface for ease of use.
- Data is saved in CSV format for compatibility with spreadsheet applications like Microsoft Excel.
- The project includes basic tests using `pytest` to ensure functionality.
