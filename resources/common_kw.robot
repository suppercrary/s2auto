*** Settings ***
Library      ../libs/BaseModel.py
Library      ../libs/LoginModel.py
Library     ../libs/StoreModel.py
Variables    ${EXECDIR}/data/store.yaml
Variables    ${EXECDIR}/data/common.yaml
Variables    ${EXECDIR}/data/login.yaml



*** Keywords ***
Get Driver And Set It As Suite Variable
    ${temp}=    Get Driver

    Set Suite Variable    ${driver}    ${temp}


Navigate To Login Page
    Open Browser

Login
    LoginModel.Set Driver    ${driver}
    ${data}=                 Set Variable         ${user_login_successfully}
    LOGIN TO SYSTEM          ${data.user_name}    ${data.password}


ChooseStore1
    StoreModel.set driver    ${driver}
    ${data}=                 Set Variable         ${no_choose_store}
    check message error from choose store       ${data.error_message}

