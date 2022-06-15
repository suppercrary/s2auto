from time import sleep

from SeleniumLibrary import SeleniumLibrary

import os
import sys

dir_name = os.path.dirname(__file__).replace(f"{os.sep}libs", "")
sys.path.append(dir_name)
from core_libs.DataHelper import locators_product

In_product = locators_product.get("In_product")


class CreateproductModel:
    def __init__(self):
        self.driver = None

    def set_driver(self, driver: SeleniumLibrary):
        self.driver = driver

    def in_product(self):
        self.driver.wait_until_page_contains_element(In_product.get("text_title"), timeout="20s")
        self.driver.click_element(In_product.get("select_product"), timeout="20s")
        self.driver.click_element(In_product.get("option_product"), timeout="20s")
        self.driver.click_element(In_product.get("text_title_product"), timeout="30s")

