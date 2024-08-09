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

Python 3.12
Poetry for dependency management
Installation
Fork the Repository:

Fork this repository to your GitHub account.
Clone the Repository:

Clone the forked repository to your local machine:

git clone https://github.com/YOUR-USERNAME/housing_price_predictor.git
cd housing_price_predictor
Install Dependencies:

Use Poetry to install the project dependencies:
poetry install
Activate the Poetry Environment:

Activate the Poetry virtual environment:

poetry shell
Running the Application
To execute the application, follow these steps:

Navigate to the Project Directory:

cd housing_price_predictor/housing_price_predictor
Run the Main Script:
Execute the main script:


python main.py
Expected Output:
The output should display a result from the Fibonacci function, which is used here as a placeholder method:

Fibonacci number at position 10 is 34
Running Tests
To run the test suite, follow these steps:

Set the Python Path:
Make sure the project root is included in the Python path:

export PYTHONPATH=$(pwd)
Execute Tests Using Poetry:


poetry run pytest
Expected Output:
The results will indicate whether the tests passed or failed.

Project Structure
The project directory is organized as follows:

plaintext
Copy code
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
