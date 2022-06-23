*** Settings ***
Resource        ../resources/store_kw.robot
Resource        ../resources/common_kw.robot
Library         ../libs/CreateproductModel.py
Variables    ${EXECDIR}/data/promotion.yaml

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
     ${data}=                           Set Variable         ${create_promotion_amount_price}
    promotion amount price  ${data.name_promotion}  ${data.start_date}  ${data.end_date}  ${data.number}  ${data.discount_amount}
