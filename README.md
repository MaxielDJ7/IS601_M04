# IS601_M04

---

# Description

📌 Command-Line Calculator (Python)

This project is a modular, professional-grade command-line calculator application built in Python. It emphasizes clean architecture, error handling, testing, and continuous integration with GitHub Actions.

✨ Features

- REPL Interface: Interactive Read-Eval-Print Loop for continuous calculations.

- Arithmetic Operations: Addition, subtraction, multiplication, division, power, and modulo.

- Calculation Management: Uses a CalculationFactory to create calculation objects and maintains a history of operations.

- Special Commands: help, history, and exit for enhanced user experience.

- Robust Error Handling: Handles invalid input and division/modulo by zero gracefully.

🧪 Testing

- Unit & Parameterized Tests with pytest for all components.

- 100% Test Coverage enforced via pytest-cov and GitHub Actions.

- Coverage Exceptions: Specific unreachable lines (e.g., pass, continue) marked with # pragma: no cover.

⚙️ CI/CD

- GitHub Actions workflow runs tests and checks coverage on every push/PR.

- Test coverage 100%.


# Getting Started

## Prequisites
- Install Python 3.10+
- Install Visual Studio Code

## Setup Instructions
- Clone Repo: `git clone git@github.com:kaw393939/module4_is601.git`
- Enter the directory: `cd module4_is601`
- Create Python Virtual Environment: `python -m venv venv`
- Activate Python Virtual Environment: `source venv/bin/activate`
- Install dependencies: `pip install -r requirements.txt`



## Executing program
- Run the tests: `pytest`
- Run the program:`python3 main.py`

# Authors

Maxiel De Jesus

# Version History

I've cloned my repositories from the module prior and added to it based on the current module tasks.

[https://github.com/MaxielDJ7/IS601_M03](https://github.com/MaxielDJ7/IS601_M03)

- Implement REPL interface for continous user interaction.
- Input validation.
- Error handling.
- Apply the DRY principle.
- Implement parameterized tests.
- Push code and configuration to GitHub and ensure that GitHub Actions runs tests successfully.

[https://github.com/MaxielDJ7/IS601_M02](https://github.com/MaxielDJ7/IS601_M02)

- Simple calculator application that includes functions for addition, subtraction, multiplication, and division.
- Tests for each calculator function using `pytest`.
- Push code and configuration to GitHub and ensure that GitHub Actions runs tests successfully.

# Acknowledgements

Professor Keith Williams Github Repository: [https://github.com/kaw393939/module4_is601](https://github.com/kaw393939/module4_is601)

