*** Settings ***
Resource        ${EXECDIR}/resources/common_kw.robot
Library         ../libs/createproduct.py

*** Keywords ***
Update Driver
    CreateProductModel.Set Driver    ${driver}

Choose store successfully
