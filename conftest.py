import pytest
import os
from dotenv import load_dotenv
import undetected_chromedriver as uc
from helpers.faker_helper import gen_user_agent
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

load_dotenv()
user_agent = gen_user_agent()

@pytest.fixture(scope="function")
def setup():
    options = uc.ChromeOptions()

    options.add_argument(f'--user-agent: {user_agent}')
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')

    driver = uc.Chrome(options=options)
    driver.delete_all_cookies()

    driver.get(os.getenv('PROXY_URL'))

    input = WebDriverWait(driver=driver, timeout=10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name="url"]')))
    input.send_keys(os.getenv('URL'))
    input.send_keys(Keys.ENTER)
 
    driver.maximize_window()

    yield driver
    driver.quit()






