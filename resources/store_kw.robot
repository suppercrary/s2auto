*** Settings ***
Resource    ../resources/common_kw.robot
Library     ../libs/StoreModel.py


*** Keywords ***
Update Driver
    StoreModel.Set Driver    ${driver}

Choose store successfully
    Choose Store
    CLICK BUTTON NEXT CHOOSE STORE
    text title
No Choose store
    title choose store
    ${data}=                          Set Variable             ${no_choose_store}
    check message error from choose store   ${data.error_message}

choose random
    random choose store
    CLICK BUTTON NEXT CHOOSE STORE

