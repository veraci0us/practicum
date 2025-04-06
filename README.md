## Automated Tests

### Quick Description
This repository contains automated UI tests for verifying the functionality of [XYZ Bank](https://www.globalsqa.com/angularJs-protractor/BankingProject/#/) site and API tests. The tests are written in Python using pytest and utilize Allure for test reporting.

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
4. **Install Docker and Docker Compose**
5. **Clone this repo for backend**:
```sh
git clone https://github.com/bondarenkokate73/simbirsoft_sdet_project.git
```
6. **Go to the root of simbirsoft_sdet_project and run:**
```sh
sudo make run
```

### Run tests in terminal
```sh
pytest -n auto
```

### View results with Alure
The report is already generated, so you can run the command to see the webpage with results:
```sh
allure serve allure-results
```