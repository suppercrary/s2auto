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

    def close_create(self):
        self.driver.click_element(Create_promotion.get("button_close"))
        self.driver.wait_until_page_contains_element(In_product.get("text_title_product"), timeout="20s")

    def option_promotion_price(self):
        sleep(1)
        self.driver.click_element(Create_promotion.get("input_amount_price"))

    def option_promotion_percent(self):
        sleep(1)
        self.driver.click_element(Create_promotion.get("input_amount_percent"))

    def option_promotion_bill(self):
        sleep(1)
        self.driver.click_element(Create_promotion.get("input_amount_bill"))

    def option_promotion_bill_percent(self):
        sleep(1)
        self.driver.click_element(Create_promotion.get("input_amount_bill_percent"))

    def option_promotion_buy_one(self):
        sleep(1)
        self.driver.click_element(Create_promotion.get("input_amount_buy_one"))

    def option_promotion_buy_percent(self):
        sleep(1)
        self.driver.click_element(Create_promotion.get("input_amount_buy_percent"))

    def option_promotion_free(self):
        sleep(1)
        self.driver.click_element(Create_promotion.get("input_amount_free"))

    def option_promotion_flash(self):
        sleep(1)
        self.driver.click_element(Create_promotion.get("input_amount_flash"))

    def click_continue(self):
        sleep(1)
        self.driver.click_button(Create_promotion.get("button_continue"))
        self.driver.wait_until_page_contains_element(Create_promotion.get("text_title_product_amount_price"), timeout="30s")

    def promotion_amount_price(self, nameproduct, startdate, enddate, number, discountamount):
        self.driver.wait_until_page_contains_element(inputs_data.get("text_title_product_amount_price"), timeout="30s")
        self.driver.input_text(inputs_data.get("input_name_product"), nameproduct, )
        self.driver.input_text(inputs_data.get("input_start_date"), startdate, )
        self.driver.input_text(inputs_data.get("input_end_date"), enddate, )
        self.driver.click_button(inputs_data.get("click_button_add_create"))
        self.driver.wait_until_element_is_visible(inputs_data.get("click_element_add_create"), timeout="30s")
        self.driver.click_element(inputs_data.get("click_element_add_create"))
        self.driver.double_click_element(inputs_data.get("button_increase_amount_buy_price"))
        self.driver.double_click_element(inputs_data.get("button_increase_price_after"))
        self.driver.double_click_element(inputs_data.get("button_increase_price_after"))
        self.driver.click_element(inputs_data.get("click_save"))
        self.driver.wait_until_element_is_visible(inputs_data.get("mess_success_create"), timeout="10s")

    def promotion_amount_percent(self, nameproduct, startdate, enddate):
        self.driver.wait_until_page_contains_element(inputs_data.get("text_title_product_amount_price"), timeout="30s")
        self.driver.input_text(inputs_data.get("input_name_product"), nameproduct, )
        self.driver.input_text(inputs_data.get("input_start_date"), startdate, )
        self.driver.input_text(inputs_data.get("input_end_date"), enddate, )
        self.driver.click_button(inputs_data.get("click_button_add_create"))
        self.driver.wait_until_element_is_visible(inputs_data.get("click_element_add_create"), timeout="30s")
        self.driver.click_element(inputs_data.get("click_element_add_create"))
        self.driver.double_click_element(inputs_data.get("button_increase_amount_buy_price"))
        self.driver.double_click_element(inputs_data.get("button_increase_price_after"))
        self.driver.double_click_element(inputs_data.get("button_increase_price_after"))
        self.driver.click_element(inputs_data.get("click_save"))
        self.driver.wait_until_element_is_visible(inputs_data.get("mess_success_create"), timeout="10s")

    def promotion_amount_bill(self, nameproduct, startdate, enddate):

        self.driver.wait_until_page_contains_element(inputs_data.get("text_title_product_amount_price"), timeout="30s")
        self.driver.input_text(inputs_data.get("input_name_product"), nameproduct, )
        self.driver.input_text(inputs_data.get("input_start_date"), startdate, )
        self.driver.input_text(inputs_data.get("input_end_date"), enddate, )
        self.driver.click_element(inputs_data.get("click_element_add_create"))
        self.driver.double_click_element(inputs_data.get("button_increase_price_bill"))
        self.driver.double_click_element(inputs_data.get("button_increase_price_after"))
        self.driver.double_click_element(inputs_data.get("button_increase_price_after"))
        self.driver.click_element(inputs_data.get("click_save"))
        self.driver.wait_until_element_is_visible(inputs_data.get("mess_success_create"), timeout="10s")

    def promotion_amount_bill_percent(self, nameproduct, startdate, enddate):

        self.driver.wait_until_page_contains_element(inputs_data.get("text_title_product_amount_price"), timeout="30s")
        self.driver.input_text(inputs_data.get("input_name_product"), nameproduct, )
        self.driver.input_text(inputs_data.get("input_start_date"), startdate, )
        self.driver.input_text(inputs_data.get("input_end_date"), enddate, )
        self.driver.click_element(inputs_data.get("click_element_add_create"))
        self.driver.double_click_element(inputs_data.get("button_increase_price_bill"))
        self.driver.double_click_element(inputs_data.get("button_increase_price_after"))
        self.driver.double_click_element(inputs_data.get("button_increase_price_after"))
        self.driver.click_element(inputs_data.get("click_save"))
        self.driver.wait_until_element_is_visible(inputs_data.get("mess_success_create"), timeout="10s")

    def promotion_amount_buy_one(self, nameproduct, startdate, enddate):
        self.driver.wait_until_page_contains_element(inputs_data.get("text_title_product_amount_price"), timeout="30s")
        self.driver.input_text(inputs_data.get("input_name_product"), nameproduct, )
        self.driver.input_text(inputs_data.get("input_start_date"), startdate, )
        self.driver.input_text(inputs_data.get("input_end_date"), enddate, )
        self.driver.click_element(inputs_data.get("button_increase_amount_buy"))
        self.driver.double_click_element(inputs_data.get("button_increase_amount_get"))
        self.driver.double_click_element(inputs_data.get("button_increase_price"))
        self.driver.click_element(inputs_data.get("click_save"))
        self.driver.wait_until_element_is_visible(inputs_data.get("mess_success_create"), timeout="10s")

    def promotion_amount_buy_percent(self, nameproduct, startdate, enddate):
        self.driver.wait_until_page_contains_element(inputs_data.get("text_title_product_amount_price"), timeout="30s")
        self.driver.input_text(inputs_data.get("input_name_product"), nameproduct, )
        self.driver.input_text(inputs_data.get("input_start_date"), startdate, )
        self.driver.input_text(inputs_data.get("input_end_date"), enddate, )
        self.driver.click_element(inputs_data.get("button_increase_amount_buy"))
        self.driver.double_click_element(inputs_data.get("button_increase_amount_get"))
        self.driver.double_click_element(inputs_data.get("button_increase_price"))
        self.driver.click_element(inputs_data.get("click_save"))
        self.driver.wait_until_element_is_visible(inputs_data.get("mess_success_create"), timeout="10s")

    def promotion_amount_free(self, nameproduct, startdate, enddate):
        self.driver.wait_until_page_contains_element(inputs_data.get("text_title_product_amount_price"), timeout="30s")
        self.driver.input_text(inputs_data.get("input_name_product"), nameproduct, )
        self.driver.input_text(inputs_data.get("input_start_date"), startdate, )
        self.driver.input_text(inputs_data.get("input_end_date"), enddate, )
        self.driver.click_element(inputs_data.get("click_save"))
        self.driver.wait_until_element_is_visible(inputs_data.get("mess_success_create"), timeout="10s")

    def promotion_amount_flash_price(self, nameproduct, startdate, enddate):
        self.driver.wait_until_page_contains_element(inputs_data.get("text_title_product_amount_price"), timeout="30s")
        self.driver.input_text(inputs_data.get("input_name_product"), nameproduct, )
        self.driver.input_text(inputs_data.get("input_start_date"), startdate, )
        self.driver.input_text(inputs_data.get("input_end_date"), enddate, )
        self.driver.click_element(inputs_data.get("click_button_add_create"))
        self.driver.wait_until_element_is_visible(inputs_data.get("click_element_add_create"), timeout="30s")
        self.driver.click_element(inputs_data.get("click_element_add_create"))
        self.driver.click_element(inputs_data.get("button_start_time"))
        self.driver.click_element(inputs_data.get("option_start_hours"))
        self.driver.click_element(inputs_data.get("button_end_time"))
        self.driver.click_element(inputs_data.get("option_end_hours"))
        self.driver.double_click_element(inputs_data.get("button_increase_price_after"))
        self.driver.click_element(inputs_data.get("click_save"))
        self.driver.wait_until_element_is_visible(inputs_data.get("mess_success_create"), timeout="10s")

    def promotion_amount_flash_percent(self, nameproduct, startdate, enddate):
        self.driver.wait_until_page_contains_element(inputs_data.get("text_title_product_amount_price"), timeout="30s")
        self.driver.input_text(inputs_data.get("input_name_product"), nameproduct, )
        self.driver.input_text(inputs_data.get("input_start_date"), startdate, )
        self.driver.input_text(inputs_data.get("input_end_date"), enddate, )
        self.driver.click_element(inputs_data.get("click_button_add_create"))
        self.driver.wait_until_element_is_visible(inputs_data.get("click_element_add_create"), timeout="30s")
        self.driver.click_element(inputs_data.get("click_element_add_create"))
        self.driver.click_element(inputs_data.get("button_start_time"))
        self.driver.click_element(inputs_data.get("option_start_hours"))
        self.driver.click_element(inputs_data.get("button_end_time"))
        self.driver.click_element(inputs_data.get("option_end_hours"))
        self.driver.click_element(inputs_data.get("option_amount"))
        self.driver.double_click_element(inputs_data.get("button_increase_price_after"))
        self.driver.click_element(inputs_data.get("click_save"))
        self.driver.wait_until_element_is_visible(inputs_data.get("mess_success_create"), timeout="10s")

    def input_name(self, nameproduc):
        self.driver.input_text(inputs_data.get("input_name_product"), nameproduc, )

    def input_start_date(self, startdate):
        self.driver.input_text(inputs_data.get("input_start_date"), startdate,)

    def input_end_date(self, enddate):
        self.driver.input_text(inputs_data.get("input_end_date"), enddate)

    def check_time(self):
        self.driver.click_element(inputs_data.get("check_run_time"))

    def input_start_time(self):
        self.driver.click_element(inputs_data.get("click_start_hour"))
        self.driver.click_element(inputs_data.get("option_start_hour"))

    def input_end_time(self):
        self.driver.click_element(inputs_data.get("click_end_hour"))
        self.driver.click_element(inputs_data.get("option_end_hour"))

    def check_limit_amount(self):
        self.driver.click_element(inputs_data.get("check_amount"))

    def input_limit_amount(self):
        self.driver.double_click_element(inputs_data.get("input_limit_amount_increase"))

    def check_limit_price(self):
        self.driver.click_element(inputs_data.get("check_price"))

    def input_limit_price(self):
        self.driver.double_click_element(inputs_data.get("input_limit_price_increase"))

    def click_create_promotion(self):
        self.driver.click_element(inputs_data.get("click_button_add_create"))

    def input_amount_price(self):
        self.driver.wait_until_element_is_visible(inputs_data.get("click_element_add_create"))
        self.driver.click_element(inputs_data.get("click_element_add_create"))
        self.driver.double_click_element(inputs_data.get("button_increase_amount_buy_price"))

    def input_price_after(self):
        self.driver.wait_until_element_is_visible(inputs_data.get("click_element_add_create"))
        self.driver.click_element(inputs_data.get("click_element_add_create"))
        self.driver.double_click_element(inputs_data.get("button_increase_price_after"))

    def input_start_time_hour(self):
        self.driver.wait_until_element_is_visible(inputs_data.get("click_element_add_create"))
        self.driver.click_element(inputs_data.get("click_element_add_create"))
        self.driver.click_element(inputs_data.get("button_start_time"))
        self.driver.click_element(inputs_data.get("option_start_hours"))

    def input_end_time_hour(self):
        self.driver.wait_until_element_is_visible(inputs_data.get("click_element_add_create"))
        self.driver.click_element(inputs_data.get("click_element_add_create"))
        self.driver.click_element(inputs_data.get("button_end_time"))
        self.driver.click_element(inputs_data.get("option_end_hours"))

    def click_price(self):
        self.driver.click_element(inputs_data.get("option_amount"))

    def input_price_or_percent(self):
        self.driver.double_click_element(inputs_data.get("button_increase_price_after"))

    def mess_error_name(self):
        self.driver.wait_until_element_is_visible(inputs_data.get("mess_error_name"), timeout="30s")

    def mess_error_start_date(self):
        self.driver.wait_until_element_is_visible(inputs_data.get("mess_error_start_day"), timeout="30s")

    def mess_error_end_date(self):
        self.driver.wait_until_element_is_visible(inputs_data.get("mess_error_end_day"), timeout="30s")

    def mess_limit_price(self):
        self.driver.wait_until_element_is_visible(inputs_data.get("mess_error_price"), timeout="30s")

    def mess_limit_amount(self):
        self.driver.wait_until_element_is_visible(inputs_data.get("mess_error_amount"), timeout="30s")

    def mess_error_start_hour(self):
        self.driver.wait_until_element_is_visible(inputs_data.get("mess_error_start_hour"), timeout="30s")

    def mess_error_end_hour(self):
        self.driver.wait_until_element_is_visible(inputs_data.get("mess_error_end_hour"), timeout="30s")

    # def mess_start_end_date(self):
    #
    # def mess_strt_end_time(self):

    def create_success(self):
        self.driver.wait_until_element_is_visible(inputs_data.get("mess_success_create"), timeout="10s")

    def create_error(self):
        self.driver.wait_until_element_is_visible(inputs_data.get("mess_error_create"), timeout="10s")


