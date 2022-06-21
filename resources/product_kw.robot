*** Settings ***
Resource        ../resources/store_kw.robot
Resource        ../resources/common_kw.robot
Library         ../libs/CreateproductModel.py

*** Keywords ***
Update Driver
    CreateproductModel.Set driver    ${driver}

in promotion
    in product
create promotion amount price
    in product
    Create promotion
input data amount price
    in product
    Create promotion
     ${data}=                           Set Variable         ${}
    LOGIN TO SYSTEM                    ${data.user_name}    ${data.password}
    input data promotion amount price
