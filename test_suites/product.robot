*** Settings ***
Resource         ../resources/product_kw.robot



Test Setup       Run Keywords                           Navigate To Login Page
                 ...                                    AND                       Get Driver And Set It As Suite Variable
                 ...                                    AND                       Login
                 ...                                    AND                       store choose successfully
                 ...                                    AND                       product_kw.Update Driver
Test Teardown    Close Browser

*** Test Cases ***
#Test_case1: in promotion
#    in promotion
#Test_case2: Create in promotion
#    create promotion amount price
#Test_case3: input data promotion amount price
#     input data amount price

#Test_case4: input data promotion amount percent
#     input data amount percent

#Test_case: input data promotion amount bill
#     input data amount bill

Test_case: input data promotion amount bill percent
     input data amount bill percent

