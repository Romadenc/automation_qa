import random
import time

import pytest
from pages.elements_page import TextBoxPage, CheckBoxPage, RadioButtonPage, WebTablePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class TestElements:
    class TestTextBox:

        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, 'https://demoqa.com/text-box')
            text_box_page.open()
            full_name, email, current_address, permanent_address = text_box_page.fill_all_fields()
            output_name, output_email, output_current_address, output_permanent_address = text_box_page.check_filled_form()
            assert full_name == output_name, f"Expected Full Name: {full_name}, but got: {output_name}"
            assert email == output_email, f"Expected Email: {email}, but got: {output_email}"
            assert current_address == output_current_address, f"Expected Current Address: {current_address}, but got: {output_current_address}"
            assert permanent_address == output_permanent_address, f"Expected Permanent Address: {permanent_address}, but got: {output_permanent_address}"

    class TestCheckBox:
        def test_check_box(self, driver):
            check_box_page = CheckBoxPage(driver, 'https://demoqa.com/checkbox')
            check_box_page.open()
            check_box_page.open_full_list()
            check_box_page.click_random_checkbox()
            input_checkbox = check_box_page.get_checked_checkboxes()
            output_checkbox = check_box_page.get_output_result()
            assert input_checkbox == output_checkbox, 'checkboxes have not been selected'

    class TestRadioButton:
        def test_radio_button(self, driver):
            radio_button_page = RadioButtonPage(driver, 'https://demoqa.com/radio-button')
            radio_button_page.open()
            radio_button_page.click_on_the_radio_button('yes')
            output_yes = radio_button_page.get_output_result()

            assert output_yes == 'Yes', f"Expected 'Yes',but got {output_yes}"
            radio_button_page.click_on_the_radio_button('impressive')

            output_impressive = radio_button_page.get_output_result()
            assert output_impressive == 'Impressive',f"Expected 'Yes',but got {output_impressive}"

    class TestWebTable:
        def test_web_table_add_person(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            new_person = web_table_page.add_new_person()
            table_result = web_table_page.check_new_added_person()
            assert new_person in table_result


        def test_web_table_search_person(self,driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            key_word = web_table_page.add_new_person()[random.randint(0, 5)]
            web_table_page.search_some_person(key_word)
            table_result = web_table_page.check_search_person()
            assert key_word in table_result,"the person was not found in the table"



