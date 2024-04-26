import time
from pages.base_page import  BasePage
from pages.elements_page import TextBoxPage
from selenium.webdriver.common.by import By


class TestElements:
    class TestTextBox:

        def test_tex_box(self, driver):
            text_box_page = TextBoxPage(driver,'https://demoqa.com/text-box')
            text_box_page.open()
            text_box_page.fill_all_fields()
            time.sleep(4)







