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
create promotion amount
    in product
    Create promotion
input data amount price
    in product
    Create promotion
    option promotion price
    click continue
     ${data}=                           Set Variable         ${create_promotion_amount_price}
    promotion amount price  ${data.name_promotion}  ${data.start_date}  ${data.end_date}  ${data.number}  ${data.discount_amount}
input data amount percent
    create promotion amount
    option promotion percent
    click continue
    ${data}=                            set variable    ${create_promotion_amount_percent}
    promotion amount percent     ${data.name_promotion}  ${data.start_date}  ${data.end_date}
input data amount bill
    create promotion amount
    option promotion bill
    click continue
    ${data}=                            set variable    ${create_promotion_amount_bill}
    promotion amount bill     ${data.name_promotion}  ${data.start_date}  ${data.end_date}
input data amount bill percent
    create promotion amount
    option promotion bill percent
    click continue
    ${data}=                            set variable    ${create_promotion_amount_bill_percent}
    promotion amount bill percent     ${data.name_promotion}  ${data.start_date}  ${data.end_date}