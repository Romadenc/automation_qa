import time

import pytest
from selenium import webdriver


@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    time.sleep(2)
    yield driver
    driver.quit()
