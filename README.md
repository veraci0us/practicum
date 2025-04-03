## Automated Tests

### Quick Description
This repository contains automated tests for verifying the functionality of [XYZ Bank](https://www.globalsqa.com/angularJs-protractor/BankingProject/#/) site's manager pager. The tests are written in Python using pytest and utilize Allure for test reporting.

### Installation
Follow these steps to set up your environment and install the necessary dependencies locally.

1. **Clone the repository:**
```sh
git clone https://github.com/veraci0us/input-fields.git
cd input-fields
```
2. **Set up a virtual environment:**
```sh
python3 -m venv venv
source venv/bin/activate
```
3. **Install dependencies:**
```sh
pip install -r requirements.txt
```

### Run tests in terminal
```sh
pytest -s
```

### View results with Alure
The report is already generated, so you can run the command to see the webpage with results:
```sh
allure serve allure-results
```