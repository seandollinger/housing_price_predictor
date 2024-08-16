Housing Price Prediction App
This repository hosts a simple application designed to predict housing prices using historical data. The project is built with Python and managed using Poetry for dependency management. The codebase includes tests to ensure correct functionality.

Table of Contents
Prerequisites
Installation
Running the Application
Running Tests
Project Structure
Prerequisites
Before getting started, ensure you have the following installed:

Python 3.11
Poetry for dependency management
Installation
Fork the Repository:
Fork this repository to your GitHub account.
Clone the Repository:
Clone the forked repository to your local machine:
bash

git clone https://github.com/YOUR-USERNAME/housing_price_predictor.git
cd housing_price_predictor
Install Dependencies:
Use Poetry to install the project dependencies:
bash

poetry install
Activate the Poetry Environment:
Activate the Poetry virtual environment:
bash

poetry shell
Running the Application
To execute the application, follow these steps:

Navigate to the Project Directory:
Navigate to the project directory:
bash

cd housing_price_predictor/housing_price_predictor
Run the Main Script:
Execute the main script:
bash

python main.py
Running main.py
To run the main.py script, execute the following command in your terminal:

bash

python main.py
Expected Output:
Since the current implementation might not produce visible output, running main.py may serve as a placeholder for future development.

Running Tests
To run the test suite for your main.py script, follow these steps:

Set the Python Path:
Ensure that the project root is included in the Python path by running the following command before executing your tests:

bash
export PYTHONPATH=$(pwd)
Run the Tests:
Use pytest to run the tests:

bash
pytest
Execute Tests Using Poetry:
Alternatively, you can run the tests using Poetry:

bash
poetry run pytest
Expected Output:
The test results will indicate whether the tests passed or failed.

Project Structure
The project directory is organized as follows:


housing_price_predictor/
├── housing_price_predictor/
│   ├── __init__.py
│   ├── main.py
├── tests/
│   ├── test_main.py
├── pyproject.toml
└── README.md
housing_price_predictor/: Contains the main application code.
tests/: Contains the test files.
pyproject.toml: Defines project dependencies and configuration for Poetry.
README.md: Provides documentation for the project.

