from time import sleep

from SeleniumLibrary import SeleniumLibrary

import os
import sys

dir_name = os.path.dirname(__file__).replace(f"{os.sep}libs", "")
sys.path.append(dir_name)
from core_libs.DataHelper import locators

store_locators = locators.get("ChooseStore")


class StoreModel:
    def __init__(self):
        self.driver = None

    def set_driver(self, driver: SeleniumLibrary):
        self.driver = driver

    def title_choose_store(self,test=False):
        self.driver.wait_until_page_contains_element(
            store_locators.get("text_title_from"), timeout="30s"
        )
        if test is False:
            sleep(3)
            self.driver.click_element(store_locators.get("button_next_choose_store"))
            self.driver.wait_until_page_contains_element(
                store_locators.get("button_next_choose_store"), timeout="20s"
            )
            self.driver.wait_until_element_is_visible(
                store_locators.get("button_next_choose_store"), timeout="10s"
            )
            self.driver.click_element(store_locators.get("button_next_choose_store"))

    def choose_store(self, test=False):
        self.driver.wait_until_page_contains_element(
            store_locators.get("text_title_from"), timeout="10s"
        )
        self.driver.wait_until_page_contains_element(
            store_locators.get("select_choose_store"), timeout="10s"
        )
        if test is False:
            sleep(3)
            self.driver.click_element(store_locators.get("select_choose_store"))
            self.driver.wait_until_page_contains_element(
                store_locators.get("option_choose_store"), timeout="20s"
            )
            self.driver.wait_until_element_is_visible(
                store_locators.get("option_choose_store"), timeout="10s"
            )
            self.driver.click_element(store_locators.get("option_choose_store"))
            self.driver.wait_until_element_is_not_visible(
                store_locators.get("option_choose_store"), timeout="10s"
            )

    def click_button_next_choose_store(self):
        self.driver.click_button(store_locators.get("button_next_choose_store"))

    def text_title(self):
        self.driver.wait_until_page_contains_element(
            store_locators.get("text_title"), timeout="30s")

    def click_button_cancel_choose_store(self):
        self.driver.click_button(
            store_locators.get("button_cancel_choose_store")
        )
        sleep(5)

    def check_message_error_from_choose_store(self, text):
        self.driver.element_text_should_be(
            store_locators.get("message_error_from"),
            text,
        )
