# Automation Entry Test

## Installation

- **Programming language**: This project requires 3.12.x of [Python](https://www.python.org/downloads/)
- **IDE**: [Visual Studio Code](https://code.visualstudio.com/download) or [Pycharm](https://www.jetbrains.com/)
  - Visual Studio Code Extensions (refer to the list in .vscode/extensions.json)

## VSCode Setup

1. To set up this project on your local machine, clone it from the GitHub repository.
2. From the command line in the project's root directory, run:
   - `python -m pip install --upgrade pip` to upgrade pip (use `python3` for MacOS).
   - `pip install pipenv` to install pipenv.
   - `pipenv install --dev` to install all dependencies.
   - `pipenv shell` to activate the virtualenv.
   - Select the Python interpreter corresponds to the virtualenv.

## Pycharm Setup

1. To set up this project on your local machine, clone it from the GitHub repository.
2. From the command line in the project's root directory, run:
   - `python -m pip install --upgrade pip` to upgrade pip (use `python3` for MacOS).
   - `pip install virtualenv` to install the virtualenv.
   - `virtualenv venv` to create the virtualenv.
   - `venv\Scripts\activate` to active the virtualenv.
   - `pip install -r requirements.txt` to install all packages.
   - Add the Python interpreter corresponds to the virtualenv.

## Running Tests in VSCode

- Run `pipenv run python -m pytest` from the command line to run all tests.
- To see the console logs, user the `-vs` option.
- To run tests by tags, use the `-m` option with the tag's names.
- Run tests with CLI arguments:
  - `pipenv run python -m pytest -vs -m demo`

## Running Tests in Pycharm

- Run `pytest` from the command line to run all tests.
- To see the console logs, user the `-vs` option.
- To run tests by tags, use the `-m` option with the tag's names.
- Run tests with CLI arguments:
  - `pytest -vs -m demo`
