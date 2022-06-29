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

close create promotion
    in product
    close create

input data amount price
    in product
    Create promotion
    option promotion price
    click continue
     ${data}=                           Set Variable         ${create_promotion_amount_price}
    promotion amount price  ${data.name_promotion}  ${data.start_date}  ${data.end_date}  ${data.number}  ${data.discount_amount}
    click save
    create_success

fail no input all field
    create promotion amount
    option promotion price
    click continue
    click save
    mess error name
    mess error start date
    mess error end date

faile no input field name
    create promotion amount
    option promotion price
    click continue
    ${data}=                            set variable    ${create_promotion_amount_price}
    input start date    ${data.start_date}
    input end date      ${data.end_date}
    click save
    mess error name

faile no input field start date
    create promotion amount
    option promotion price
    click continue
    ${data}=                            set variable    ${create_promotion_amount_price}
    input name    ${data.name_promotion}
    input end date      ${data.end_date}
    click save
    mess error start date

faile no input field end date
    create promotion amount
    option promotion price
    click continue
    ${data}=                            set variable    ${create_promotion_amount_price}
    input name    ${data.name_promotion}
    input start date      ${data.start_date}
    click save
    mess error end date

faile no protion
    create promotion amount
    option promotion price
    click continue
    ${data}=                            set variable    ${create_promotion_amount_price}
    input name    ${data.name_promotion}
    input start date      ${data.start_date}
    input end date      ${data.end_date}
    click save
    create error

faile no limit amount
    in product
    Create promotion
    option promotion price
    click continue
    check limit amount
     ${data}=                           Set Variable         ${create_promotion_amount_price}
    promotion amount price  ${data.name_promotion}  ${data.start_date}  ${data.end_date}  ${data.number}  ${data.discount_amount}
    mess limit amount

faile no limit price
    in product
    Create promotion
    option promotion price
    click continue
    check limit price
     ${data}=                           Set Variable         ${create_promotion_amount_price}
    promotion amount price  ${data.name_promotion}  ${data.start_date}  ${data.end_date}  ${data.number}  ${data.discount_amount}
    mess limit price

input data amount percent
    create promotion amount
    option promotion percent
    click continue
    ${data}=                            set variable    ${create_promotion_amount_percent}
    promotion amount percent     ${data.name_promotion}  ${data.start_date}  ${data.end_date}
    click save
    create_success

percent fail no input all field
    create promotion amount
    option promotion percent
    click continue
    click save
    mess error name
    mess error start date
    mess error end date

percent faile no input field name
    create promotion amount
    option promotion percent
    click continue
    ${data}=                            set variable    ${create_promotion_amount_percent}
    input start date    ${data.start_date}
    input end date      ${data.end_date}
    click save
    mess error name

percent faile no input field start date
    create promotion amount
    option promotion percent
    click continue
    ${data}=                            set variable    ${create_promotion_amount_percent}
    input name    ${data.name_promotion}
    input end date      ${data.end_date}
    click save
    mess error start date

percent faile no input field end date
    create promotion amount
    option promotion percent
    click continue
    ${data}=                            set variable    ${create_promotion_amount_percent}
    input name    ${data.name_promotion}
    input start date      ${data.start_date}
    click save
    mess error end date

percent faile no protion
    create promotion amount
    option promotion percent
    click continue
    ${data}=                            set variable    ${create_promotion_amount_percent}
    input name    ${data.name_promotion}
    input start date      ${data.start_date}
    input end date      ${data.end_date}
    click save
    create error

percent faile no limit amount
    in product
    Create promotion
    option promotion percent
    click continue
    check limit amount
     ${data}=                           Set Variable         ${create_promotion_amount_percent}
    promotion amount price  ${data.name_promotion}  ${data.start_date}  ${data.end_date}  ${data.number}  ${data.discount_amount}
    click save
    mess limit amount

percent faile no limit price
    in product
    Create promotion
    option promotion percent
    click continue
    check limit price
     ${data}=                           Set Variable         ${create_promotion_amount_percent}
    promotion amount price  ${data.name_promotion}  ${data.start_date}  ${data.end_date}  ${data.number}  ${data.discount_amount}
    click save
    mess limit price

input data amount bill
    create promotion amount
    option promotion bill
    click continue
    ${data}=                            set variable    ${create_promotion_amount_bill}
    promotion amount bill     ${data.name_promotion}  ${data.start_date}  ${data.end_date}
    click save
    create_success

bill fail no input all field
    create promotion amount
    option promotion bill
    click continue
    click save
    mess error name
    mess error start date
    mess error end date

bill faile no input field name
    create promotion amount
    option promotion bill
    click continue
    ${data}=                            set variable    ${create_promotion_amount_bill}
    input start date    ${data.start_date}
    input end date      ${data.end_date}
    click save
    mess error name

bill faile no input field start date
    create promotion amount
    option promotion bill
    click continue
    ${data}=                            set variable    ${create_promotion_amount_bill}
    input name    ${data.name_promotion}
    input end date      ${data.end_date}
    click save
    mess error start date

bill faile no input field end date
    create promotion amount
    option promotion bill
    click continue
    ${data}=                            set variable    ${create_promotion_amount_bill}
    input name    ${data.name_promotion}
    input start date      ${data.start_date}
    click save
    mess error end date

bill faile no limit price
    in product
    Create promotion
    option promotion bill
    click continue
    check limit price
     ${data}=                           Set Variable         ${create_promotion_amount_bill}
    promotion amount bill     ${data.name_promotion}  ${data.start_date}  ${data.end_date}
    click save
    mess limit price

input data amount bill percent
    create promotion amount
    option promotion bill percent
    click continue
    ${data}=                            set variable    ${create_promotion_amount_bill_percent}
    promotion amount bill percent     ${data.name_promotion}  ${data.start_date}  ${data.end_date}
    click save
    create_success

bill percent fail no input all field
    create promotion amount
    option promotion bill percent
    click continue
    click save
    mess error name
    mess error start date
    mess error end date

bill percent faile no input field name
    create promotion amount
    option promotion bill percent
    click continue
    ${data}=                            set variable    ${create_promotion_amount_bill_percent}
    input start date    ${data.start_date}
    input end date      ${data.end_date}
    click save
    mess error name

bill percent faile no input field start date
    create promotion amount
    option promotion bill percent
    click continue
    ${data}=                            set variable    ${create_promotion_amount_bill_percent}
    input name    ${data.name_promotion}
    input end date      ${data.end_date}
    click save
    mess error start date

bill percent faile no input field end date
    create promotion amount
    option promotion bill percent
    click continue
    ${data}=                            set variable    ${create_promotion_amount_bill_percent}
    input name    ${data.name_promotion}
    input start date      ${data.start_date}
    click save
    mess error end date

bill percent faile no limit price
    in product
    Create promotion
    option promotion bill percent
    click continue
    check limit price
     ${data}=                           Set Variable         ${create_promotion_amount_bill_percent}
    promotion amount bill percent     ${data.name_promotion}  ${data.start_date}  ${data.end_date}
    click save
    mess limit price

input data amount buy one
    create promotion amount
    option promotion buy one
    click continue
    ${data}=                            set variable    ${create_promotion_amount_buy_one}
    promotion amount buy one     ${data.name_promotion}  ${data.start_date}  ${data.end_date}
    click save
    create_success

input data amount buy percent
    create promotion amount
    option promotion buy percent
    click continue
    ${data}=                            set variable    ${create_promotion_amount_buy_percent}
    promotion amount buy percent     ${data.name_promotion}  ${data.start_date}  ${data.end_date}
    create_success

input data amount free
    create promotion amount
    option promotion free
    click continue
    ${data}=                            set variable    ${create_promotion_amount_free}
    promotion amount free     ${data.name_promotion}  ${data.start_date}  ${data.end_date}
    click save
    create_success

free fail no input all field
    create promotion amount
    option promotion free
    click continue
    click save
    mess error name
    mess error start date
    mess error end date

free faile no input field name
    create promotion amount
    option promotion free
    click continue
    ${data}=                            set variable    ${create_promotion_amount_free}
    input start date    ${data.start_date}
    input end date      ${data.end_date}
    click save
    mess error name

free faile no input field start date
    create promotion amount
    option promotion free
    click continue
    ${data}=                            set variable    ${create_promotion_amount_free}
    input name    ${data.name_promotion}
    input end date      ${data.end_date}
    click save
    mess error start date

free faile no input field end date
    create promotion amount
    option promotion free
    click continue
    ${data}=                            set variable    ${create_promotion_amount_free}
    input name    ${data.name_promotion}
    input start date      ${data.start_date}
    click save
    mess error end date

free faile no limit amount
    in product
    Create promotion
    option promotion free
    click continue
    check limit amount
     ${data}=                           Set Variable         ${create_promotion_amount_free}
    promotion amount bill percent     ${data.name_promotion}  ${data.start_date}  ${data.end_date}
    click save
    mess limit amount

input data price flash
    create promotion amount
    option promotion flash
    click continue
    ${data}=                            set variable    ${create_promotion_amount_flash}
    promotion amount flash price     ${data.name_promotion_price}  ${data.start_date}  ${data.end_date}
    click save
    create_success

input data percent flash
    create promotion amount
    option promotion flash
    click continue
    ${data}=                            set variable    ${create_promotion_amount_flash}
    promotion amount flash percent     ${data.name_promotion_percent}  ${data.start_date}  ${data.end_date}
    click save
    create_success

flash fail no input all field
    create promotion amount
    option promotion flash
    click continue
    click save
    mess error name
    mess error start date
    mess error end date

flash faile no input field name
    create promotion amount
    option promotion flash
    click continue
    ${data}=                            set variable    ${create_promotion_amount_flash}
    input start date    ${data.start_date}
    input end date      ${data.end_date}
    click save
    mess error name

flash faile no input field start date
    create promotion amount
    option promotion flash
    click continue
    ${data}=                            set variable    ${create_promotion_amount_flash}
    input name    ${data.name_promotion_percent}
    input end date      ${data.end_date}
    click save
    mess error start date

flash faile no input field end date
    create promotion amount
    option promotion flash
    click continue
    ${data}=                            set variable    ${create_promotion_amount_flash}
    input name    ${data.name_promotion_price}
    input start date      ${data.start_date}
    click save
    mess error end date

flash faile no protion
    create promotion amount
    option promotion flash
    click continue
    ${data}=                            set variable    ${create_promotion_amount_flash}
    input name    ${data.name_promotion_price}
    input start date      ${data.start_date}
    input end date      ${data.end_date}
    click save
    create error

flash faile no limit amount
    in product
    Create promotion
    option promotion flash
    click continue
    check limit amount
     ${data}=                           Set Variable         ${create_promotion_amount_flash}
    promotion amount flash price    ${data.name_promotion_price}  ${data.start_date}  ${data.end_date}
    click save
    mess limit amount

flash faile no limit price
    in product
    Create promotion
    option promotion flash
    click continue
    check limit price
     ${data}=                           Set Variable         ${create_promotion_amount_flash}
    promotion amount flash price    ${data.name_promotion_price}  ${data.start_date}  ${data.end_date}
    mess limit price
