from time import sleep

from SeleniumLibrary import SeleniumLibrary

import os
import sys

dir_name = os.path.dirname(__file__).replace(f"{os.sep}libs", "")
sys.path.append(dir_name)
from core_libs.DataHelper import locators
createproduct = locators.get("CreateProduct")

class CreateProductModel:
    def __init__(self):
        self.driver=None

    def set_driver(self, driver: SeleniumLibrary):
        self.driver = driver

    def title_chose(self):
        self.driver.wait_until_page_contains_element(
            createproduct.get("text_title"), timeout="30s")

    def select_product(self):
        self.driver.click_element("select_product")

