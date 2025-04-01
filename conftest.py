import pytest
import os
from dotenv import load_dotenv
from helpers.faker_helper import gen_user_agent
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

load_dotenv()
user_agent = gen_user_agent()

def is_github_actions():
    return 'GITHUB_ACTIONS' in os.environ

def run_on_github():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')

    driver = webdriver.Chrome(options=options)
    driver.get(os.getenv('URL'))
    
    return driver

@pytest.fixture(scope="function")
def setup():

    if is_github_actions():
        driver = run_on_github()
    else:
        options = webdriver.ChromeOptions()
        options.add_argument(f'--user-agent: {user_agent}')

        service = Service(ChromeDriverManager.install())
        driver = webdriver.Chrome(options=options, service=service)
        
        driver.delete_all_cookies()

    driver.get(os.getenv('PROXY_URL'))

    input = WebDriverWait(driver=driver, timeout=10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name="url"]')))
    input.send_keys(os.getenv('URL'))
    input.send_keys(Keys.ENTER)
 
    driver.maximize_window()

    yield driver
    driver.quit()





