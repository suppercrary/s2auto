*** Settings ***
Resource    ../resources/common_kw.robot
Library     ../libs/LoginModel.py


*** Keywords ***
Update Driver
    LoginModel.Set Driver    ${driver}


Login With Correct Data
    ${data}=           Set Variable         ${user_login_successfully}
    LOGIN TO SYSTEM    ${data.user_name}    ${data.password}

Login with null username
    ${data}=                           Set Variable         ${user_login_null_user_name}
    LOGIN TO SYSTEM                    ${data.user_name}    ${data.password}
    CHECK MESSAGE ERROR INPUT LOGIN    users_name           ${data.error_message}

Login with null password
    ${data}=                           Set Variable         ${user_login_null_password}
    LOGIN TO SYSTEM                    ${data.user_name}    ${data.password}
    CHECK MESSAGE ERROR INPUT LOGIN    password             ${data.error_message}

Login with null username and password
    ${data}=                           Set Variable         ${user_login_null_user_name_and_password}
    LOGIN TO SYSTEM                    ${data.user_name}    ${data.password}
    CHECK MESSAGE ERROR INPUT LOGIN    users_name           ${data.error_message_user_name}
    CHECK MESSAGE ERROR INPUT LOGIN    password             ${data.error_message_password}

Login with incorrect username
    ${data}=                          Set Variable             ${user_login_error_user_name}
    LOGIN TO SYSTEM                   ${data.user_name}        ${data.password}
    CHECK MESSAGE ERROR FROM LOGIN    ${data.error_message}

Login with incorrect password
    ${data}=                          Set Variable             ${user_login_error_password}
    LOGIN TO SYSTEM                   ${data.user_name}        ${data.password}
    CHECK MESSAGE ERROR FROM LOGIN    ${data.error_message}

Login with incorrect username and password
    ${data}=                          Set Variable             ${user_login_error_user_name_and_password}
    LOGIN TO SYSTEM                   ${data.user_name}        ${data.password}
    CHECK MESSAGE ERROR FROM LOGIN    ${data.error_message}
