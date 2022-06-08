from SeleniumLibrary import SeleniumLibrary
import os
import sys

dir_name = os.path.dirname(__file__).replace(f"{os.sep}libs", "")
sys.path.append(dir_name)

from core_libs.DataHelper import locators

login_locators = locators.get("Login")


class LoginModel:
    def __init__(self):
        self.driver = None

    def set_driver(self, driver: SeleniumLibrary):
        self.driver = driver

    def login_to_system(self, username, password):
        print(self.driver)
        self.driver.input_text(
            login_locators.get("input_user_name"),
            username,
        )
        self.driver.input_text(
            login_locators.get("input_password"),
            password,
        )
        self.driver.click_button(login_locators.get("button_login"))

    def check_message_error_input_login(self, name_input, text):
        locator = (
            login_locators.get("message_error_user_name")
            if name_input == "users_name"
            else login_locators.get("message_error_password")
        )
        self.driver.element_text_should_be(locator, text)

    def check_message_error_from_login(self, text):
        self.driver.element_text_should_be(
            login_locators.get("message_error_from"),
            text,
        )

    def check_title_from_login(self, text):
        self.driver.element_text_should_be(
            login_locators.get("title_from_login"),
            text,
        )
