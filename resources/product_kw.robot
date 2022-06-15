*** Settings ***

Resource        ../resources/common_kw.robot
Library         ../libs/CreateproductModel.py

*** Keywords ***
Update Driver
    CreateproductModel.Set driver    ${driver}

in product
    In product
