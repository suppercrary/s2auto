*** Settings ***
Resource         ../resources/product_kw.robot
Resource         ../resources/store_kw.robot
Resource         ../resources/common_kw.robot

Test Setup       Run Keywords                           Navigate To Login Page
                 ...                                    AND                       Get Driver And Set It As Suite Variable
                 ...                                    AND                       Login
                 ...                                    AND                       Choose store successfully
                 ...                                    AND                       Update Driver
Test Teardown    Close Browser
*** Test Cases ***
Test_case1: in product
    in product