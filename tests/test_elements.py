import pytest
from pages.elements_page import TextBoxPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class TestElements:
    class TestTextBox:

        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, 'https://demoqa.com/text-box')
            text_box_page.open()
            text_box_page.fill_all_fields()



