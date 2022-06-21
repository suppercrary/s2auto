*** Settings ***
Library      ../libs/BaseModel.py
Library      ../libs/LoginModel.py
Library     ../libs/StoreModel.py
Variables    ${EXECDIR}/data/store.yaml
Variables    ${EXECDIR}/data/common.yaml
Variables    ${EXECDIR}/data/login.yaml
Variables    ${EXECDIR}/data/promotion.yaml



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

store choose successfully
    StoreModel.Set Driver    ${driver}
    store_successfully
