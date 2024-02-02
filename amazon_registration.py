from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

sleep(1)

# Amazon Logo, CSS
driver.find_element(By.CSS_SELECTOR, '.a-icon.a-icon-logo')

# Create Account, XPATH
driver.find_element(By.XPATH, "//h1[contains(text(), 'Create account')]")

# Your Name, ID
driver.find_element(By.ID, 'ap_customer_name')

# Email, ID
driver.find_element(By.ID, 'ap_email')

# Password, ID, CSS, XPATH
driver.find_element(By.ID, 'ap_password')
driver.find_element(By.CSS_SELECTOR, "[placeholder='At least 6 characters']")
driver.find_element(By.XPATH, "//input[@name='password']")

# Passwords must be at least 6 characters, XPATH
driver.find_element(By.XPATH,"//div[contains(text(),'Passwords must be at least 6 characters.')]")

# Re-enter password, ID
driver.find_element(By.ID, 'ap_password_check')

# Continue button, ID (I don't see 'Create your Amazon account' text on the button)
driver.find_element(By.ID, 'continue')

# Conditions of use, XPATH, CSS
driver.find_element(By.XPATH, "//a[contains(@href, 'condition_of_use')]")
driver.find_element(By.CSS_SELECTOR, "[href*='condition_of_use']")

# Privacy notice, CSS
driver.find_element(By.CSS_SELECTOR, "[href*='notification_privacy_notice']")

# Sign in, XPATH
driver.find_element(By.XPATH,"//a[contains(text(), 'Sign in')]")
