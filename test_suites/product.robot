*** Settings ***
Resource         ../resources/store_kw.robot
Test Setup       Run Keywords                           Navigate To Login Page
                 ...                                    AND                       Get Driver And Set It As Suite Variable
                 ...                                    AND                       Login
                 ...                                    AND                       Update Driver
                 ...                                    AND
Test Teardown    Close Browser