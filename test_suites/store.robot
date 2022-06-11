*** Settings ***
Resource         ../resources/store_kw.robot
Test Setup       Run Keywords                           Navigate To Login Page    
                 ...                                    AND                       Get Driver And Set It As Suite Variable
                 ...                                    AND                       Login
                 ...                                    AND                       Update Driver
Test Teardown    Close Browser

*** Test Cases ***
#Case_1: Choose random successfully
#    choose random

Case_2:Choose store name successfully
    choose store name

#Case_3: Choose store successfully
#   Choose store successfully
#
#Case_4: No Choose store
#    No Choose store



