import os
import sys

dir_name = os.path.dirname(__file__).replace(f"{os.sep}libs", "")
sys.path.append(dir_name)
from SeleniumLibrary import SeleniumLibrary
from core_libs.Utility import install_chrome_driver
from core_libs.DataHelper import common_data


class BaseModel:
    def __init__(self):
        self.driver = SeleniumLibrary()
        install_chrome_driver()

    def get_driver(self):
        return self.driver

    def open_browser(self, url=common_data.get("URL"), browser="chrome"):
        self.driver.open_browser(url=url, browser=browser)
        self.driver.maximize_browser_window()

    def close_all_browsers(self):
        self.driver.close_all_browsers()

    def close_browser(self):
        self.driver.close_browser()
