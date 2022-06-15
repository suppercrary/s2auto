*** Settings ***
Resource         ../resources/product_kw.robot


Test Setup       Run Keywords                           Navigate To Login Page
                 ...                                    AND                       Get Driver And Set It As Suite Variable
                 ...                                    AND                       Login
                 ...                                    AND                       store choose successfully
                 ...                                    AND                       product_kw.Update Driver
Test Teardown    Close Browser

*** Test Cases ***
Test_case1: in promotion
    in promotion
#Test_case2: Create in promotion
