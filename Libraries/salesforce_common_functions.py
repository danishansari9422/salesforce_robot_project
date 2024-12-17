# salesforce_custom_keywords.py
from robot.api.deco import keyword
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys



def login_to_salesforce(username, password):
    # Set up the WebDriver (e.g., using Chrome)
    driver = webdriver.Chrome()  # Adjust path as needed

    try:
        # Open Salesforce login page
        driver.get("https://login.salesforce.com/")

        # Find the username and password fields and input the credentials
        username_field = driver.find_element(By.ID, "username")
        password_field = driver.find_element(By.ID, "password")

        username_field.send_keys(username)
        password_field.send_keys(password)

        # Submit the login form
        password_field.send_keys(Keys.RETURN)

        # Wait for the login to complete (you might want to add more robust waiting logic here)
        driver.implicitly_wait(10)  # Wait for the page to load after login

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        driver.quit()  # Close the browser

