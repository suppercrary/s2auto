import os
import sys

dir_name = os.path.dirname(__file__).replace(f"{os.sep}libs", "")
sys.path.append(dir_name)

from core_libs.DataHelper import locators

unit_locators = locators.get("Unit")


class UnitModel:
    def go_to_page_unit(self):
        self.driver.click_element(unit_locators.get("menu_category"))
        self.driver.wait_until_element_is_visible(
            unit_locators.get("menu_category_unit"), timeout="10s"
        )
        self.driver.click_element(unit_locators.get("menu_category_unit"))
