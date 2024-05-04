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
            full_name, email, current_address, permanent_address = text_box_page.fill_all_fields()
            output_name, output_email, output_current_address, output_permanent_address = text_box_page.check_filled_form()
            assert full_name == output_name
            assert email == output_email
            assert current_address == output_current_address
            assert permanent_address == output_permanent_address



