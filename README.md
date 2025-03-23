# PytestPythonPlayWright
This is a sample project making use of Python &amp; PlayWright for Web E2E Automation using Gherkins

## How to Run it Guide

### Step 1 - 

- Install [Python](https://www.python.org/downloads/) 
- if you're on a Mac, you can check in your terminal with `python3 --version` & `pip3 --version`

### Step 2 - 
- Choose your IDE, in my case I used [PyCharm Community Edition](https://www.jetbrains.com/products/compare/?product=pycharm-ce&product=pycharm)

### Step 3 -
- use pip (Package installer for Python) to install "pytest" which serves as a testing framework that allows us to execute PlayWright tests using the playwright-pytest plugin
- on your terminal, enter this >> `pip install pytest` (there is another way to do this via the IDE PyCharm under the Python interpreter settings)
- <img width="450" alt="image" src="https://github.com/user-attachments/assets/c9b53b29-1064-4ac8-a5da-0b2033c98f76" />
- Also, >> `pip install pytest-playwright` and finally, `playwright install`
- For using Gherkins /Cucumber BDD tests, you'd need to >> `pip3 install pytest-bdd`
- Everything's good to go at this point.

### Step 4 - 

- you can simply right click `test_pytest-bddTest.py` from your IDE
- (OR) you can use terminal commands -> somthing like `pytest <filename.py>::test_functionName` (SYNTAX)
