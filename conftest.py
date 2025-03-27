import pytest
import os
from dotenv import load_dotenv
from selenium import webdriver

load_dotenv()

@pytest.fixture
def setup():
    driver = webdriver.Chrome()
    driver.get(os.getenv('URL'))
    driver.maximize_window()
    yield driver
    driver.quit()