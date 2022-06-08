import os
import sys
import yaml
import json
from datetime import datetime, timedelta
import chromedriver_autoinstaller

dir_name = os.path.dirname(__file__).replace(f"{os.sep}core_libs", "")
sys.path.append(dir_name)


def install_chrome_driver():
    plf = sys.platform
    supported_plf = ["win32", "linux", "linux2","win11"]
    if plf in supported_plf:
        chromedriver_autoinstaller.install()


def get_env(key: str):
    return os.environ.get(key.upper())


def read_yaml(file):
    with open(file, "r") as f:
        return yaml.safe_load(f)


def read_json(file):
    with open(file, "r") as f:
        return json.load(f)
