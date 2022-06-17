*** Settings ***
Resource        ../resources/store_kw.robot
Resource        ../resources/common_kw.robot
Library         ../libs/CreateproductModel.py

*** Keywords ***
Update Driver
    CreateproductModel.Set driver    ${driver}

in promotion
    In product
create promotion amount price
    Create promotion
