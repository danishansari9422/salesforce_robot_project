*** Settings ***
Library        ../Libraries/salesforce_common_functions.py

*** Variables ***
${USERNAME}       smartestuser1@relanto.ai
${PASSWORD}       Test1234

*** Test Cases ***
Login To Salesforce

    Login To Salesforce    ${USERNAME}    ${PASSWORD}
