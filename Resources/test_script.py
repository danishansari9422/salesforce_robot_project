from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Configure Chrome options
options = Options()
# Ensure it runs in a non-headless mode for visibility
# Do not include options.add_argument("--headless") to allow GUI
options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("--window-size=1920x1080")
driver = webdriver.Chrome(options=options)

# Example Test
driver.get("https://www.google.com")
print(driver.title)
driver.quit()
