from selenium import webdriver
from selenium.webdriver.common.by import By


def initialize_browser():
    options = webdriver.ChromeOptions()
    options.add_argument('--no-sandbox')
    return webdriver.Chrome(options=options)


def login_to_salesforce(username, password):
    # Salesforce login URL
    login_url = "https://login.salesforce.com/"

    # Initialize browser and open login page
    driver = initialize_browser()
    driver.get(login_url)

    # Locate username and password fields, enter credentials, and log in
    driver.find_element(By.ID, "username").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "Login").click()

    # Check if login is successful by verifying the page title
    if "Home" in driver.title:  # Replace with actual validation logic
        print("Login successful")
    else:
        print("Login failed")
    driver.quit()
