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
            full_name, email, current_address, permanent_address = text_box_page.check_filled_form()
            print(f"Full Name: {full_name}")
            print(f"Email: {email}")
            print(f"Current Address: {current_address}")
            print(f"Permanent Address: {permanent_address}")



