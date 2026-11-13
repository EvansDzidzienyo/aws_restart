# AWS re/Start Python Labs

This repository contains introductory Python exercises and lab scripts retained from AWS re/Start learning. The examples cover core Python syntax and basic data handling; they are learning exercises, not production applications or deployed AWS infrastructure.

## Topics represented

| File | Topic |
|---|---|
| `labs.py` | Numeric and Boolean data types |
| `for-loop.py` | `for` loops and ranges |
| `lab3.py` | Strings, input, concatenation, and formatting |
| `lab4.py` | Lists, tuples, and dictionaries |
| `lab5.py` | Mixed data types and iteration |
| `lab6.py` | Reading and validating a vehicle inventory CSV |
| `lab7.py` | Conditional logic and user input |
| `lab8.py` | A simple number-guessing loop |
| `car_fleet.csv` | Sample vehicle inventory data used by `lab6.py` |

## Requirements

- Python 3.10 or later
- No third-party packages are required to run the examples.
- `pytest` is required only to run the automated tests.

## Run an exercise

From the repository directory:

```bash
python for-loop.py
python lab3.py
python lab4.py
python lab5.py
python lab6.py
python lab7.py
python lab8.py
python labs.py
```

The scripts that request input are interactive. Run `lab6.py` from the repository directory so it can find `car_fleet.csv`.

## Run tests

Install pytest if needed:

```bash
python -m pip install pytest
python -m pytest -q
```

GitHub Actions checks Python syntax and runs the tests on pushes and pull requests.

## Scope and limitations

- These are introductory exercises, not evidence of a production data pipeline or cloud deployment.
- The vehicle CSV is a small sample dataset used to demonstrate file handling.
- The repository does not currently provision or configure AWS services.
