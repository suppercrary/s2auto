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
Test_case2: Create in promotion
    create promotion amount

Test_case3: input data promotion amount price
     input data amount price

Test_case4: input data promotion amount percent
     input data amount percent

Test_case5: input data promotion amount bill
     input data amount bill

Test_case6: input data promotion amount bill percent
     input data amount bill percent

Test_case7: input data promotion amount buy one
     input data amount buy one

Test_case8: input data promotion amount buy percent
     input data amount buy percent

Test_case9: input data promotion amount free
     input data amount free

Test_case10: input data promotion price flash
     input data price flash

Test_case11: input data promotion percent flash
     input data percent flash


