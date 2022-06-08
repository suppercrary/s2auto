*** Settings ***
Resource          ../resources/login_kw.robot
Test Setup        Run Keywords                           Navigate To Login Page    
                  ...                                    AND                       Get Driver And Set It As Suite Variable
                  ...                                    AND                       Update Driver
Test Teardown     Close Browser
*** Test Cases ***

Case_1: Login With Correct Data
    Login With Correct Data

Case_2: Login with null username
    Login with null username

Case_3: Login with null password
    Login with null password

Case_4: Login with null username and password
    Login with null username and password
