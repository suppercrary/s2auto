import os
import sys

dir_name = os.path.dirname(__file__).replace(f"{os.sep}core_libs", "")
sys.path.append(dir_name)
from core_libs.Utility import read_yaml

path = os.path.dirname(__file__).replace("core_libs", "")
url_data = f"{path}{os.sep}locators{os.sep}locator.yaml"

c_path = f"{path}{os.sep}data{os.sep}common.yaml"
locators = read_yaml(url_data)
common_data = read_yaml(c_path)
