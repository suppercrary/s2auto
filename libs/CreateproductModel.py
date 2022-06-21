from time import sleep

from SeleniumLibrary import SeleniumLibrary

import os
import sys

dir_name = os.path.dirname(__file__).replace(f"{os.sep}libs", "")
sys.path.append(dir_name)
from core_libs.DataHelper import locators_product

In_product = locators_product.get("In_product")
Create_promotion = locators_product.get("Create_promotion")
inputs_data = locators_product.get("Create_Product_Amount_Price")

class CreateproductModel:
    def __init__(self):
        self.driver = None

    def set_driver(self, driver: SeleniumLibrary):
        self.driver = driver

    def in_product(self):
        self.driver.wait_until_page_contains_element(In_product.get("text_title"), timeout="30s")
        t = self.driver.find_elements(In_product.get("select_product"))
        for i in t:
            if self.driver.get_text(i) == "Quản Lý Sản Phẩm":
                self.driver.click_element(i)
        self.driver.click_element(In_product.get("option_product"))
        self.driver.wait_until_page_contains_element(In_product.get("text_title_product"), timeout="20s")

    def create_promotion(self):
        self.driver.click_element(Create_promotion.get("button_create"))
        self.driver.wait_until_page_contains_element(Create_promotion.get("text_title_Create"), timeout="30s")
        sleep(2)
        self.driver.click_element(Create_promotion.get("input_amount_price"))
        self.driver.click_button(Create_promotion.get("button_continue"))
        self.driver.wait_until_page_contains_element(Create_promotion.get("text_title_product_amount_price"), timeout="30s")
    def promotion_amount_price(self, nameproduct, startdate, enddate, number, discountamount):
        self.driver.wait_until_page_contains_element(inputs_data.get("text_title_product_amount_price"), timeout="30s")
        self.driver.input_text(inputs_data.get("input_name_product"), nameproduct, )
        self.driver.input_text(inputs_data.get("input_start_date"), startdate, )
        sleep(3)
        self.driver.input_text(inputs_data.get("input_end_date"), enddate, )
        sleep(3)
        self.driver.click_button(inputs_data.get("click_button_add_create"))
        sleep(3)
        # self.driver.click_element(inputs_data.get("click_element_add_create"))
        self.driver.input_text(inputs_data.get("input_number"), number, )
        self.driver.input_text(inputs_data.get("input_discount_amount"), discountamount, )
        self.driver.click_element(inputs_data.get("click_save"))

