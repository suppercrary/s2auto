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

Test_case3: close create
     close create promotion

Test_case4:
    input data amount price

Test_case5:
    fail no input all field

Test_case6:
    faile no input field name

Test_case7:
    faile no input field start date

Test_case8:
    faile no input field end date

Test_case9:
    faile no protion
Test_case10:
    faile no limit amount

Test_case11:
    faile no limit price

Test_case12:
    input data amount percent

Test_case13:
    percent fail no input all field

Test_case14:
    percent faile no input field start date

Test_case15:
    percent faile no input field end date

Test_case16:
    percent faile no protion

Test_case17:
    percent faile no limit amount

Test_case18:
    percent faile no limit price

Test_case19:
    input data amount bill

Test_case20:
    bill fail no input all field

Test_case21:
    bill faile no input field name

Test_case22:
    bill faile no input field start date

Test_case23:
    bill faile no input field end date

Test_case24:
    bill faile no limit price

Test_case25:
    input data amount bill percent

Test_case26:
    bill percent fail no input all field

Test_case27:
    bill percent faile no input field name

Test_case28:
    bill percent faile no input field start date

Test_case29:
    bill percent faile no input field end date

Test_case30:
    bill percent faile no limit price

Test_case31:
    input data amount buy one

Test_case32:
    input data amount buy percent

Test_case33:
    input data amount free

Test_case34:
    free fail no input all field

Test_case35:
    free faile no input field name

Test_case36:
    free faile no input field start date

Test_case37:
    free faile no input field end date

Test_case38:
    free faile no limit amount

Test_case39:
    input data price flash

Test_case40:
    input data percent flash

Test_case41:
    flash fail no input all field

Test_case42:
    flash faile no input field name

Test_case43:
    flash faile no input field start date

Test_case44:
    flash faile no input field end date

Test_case45:
    flash faile no protion

Test_case46:
    flash faile no limit amount

Test_case47:
    flash faile no limit price

Test_case48:

Test_case49:

Test_case50:

Test_case51:

Test_case52:






