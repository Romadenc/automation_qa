import time

import pytest
from selenium import webdriver


@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.maximize_window()
    time.sleep(3)
    yield driver
    driver.quit()
