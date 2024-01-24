# HOMEWORK 1ST PART

# Amazon logo, search by XPATH, $x("//i[@aria-label='Amazon']")
# Email field, search by ID, “ap_email”
# Continue button, search by ID, "continue"
# Conditions of use link, search by XPATH, $x("//a[contains(@href, 'condition_of_use')]")
# Privacy Notice link, search by XPATH, $x("//a[contains(@href, 'notification_privacy_notice')]")
# Need help link, search by XPATH, $x("//span[@class='a-expander-prompt']")
# Forgot your password link, search by ID, "auth-fpp-link-bottom"
# Other issues with Sign-In link, search by ID, "ap-other-signin-issues-link"
# Create your Amazon account button, search by ID, "createAccountSubmit"

# HOMEWORK 2ND PART

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

# Test Case: Users can navigate to SignIn page
# 1. Open https://www.target.com/
driver.get("https://www.target.com/")

# 2. Click SignIn button
driver.find_element(By.XPATH, "//span[@class='styles__LinkText-sc-1e1g60c-3 dZfgoT h-margin-r-x3']").click()
sleep(5)

# 3. Click SignIn from side navigation
driver.find_element(By.XPATH,"//a[@data-test='accountNav-signIn']").click()
sleep(5)

# 4. Verify SignIn page opened:

# “Sign in to your Target account” text is shown,
# driver.find_element(By. XPATH, "//h1[contains(@class, 'styles__StyledHeading')]")
expected_text = "Sign in to your Target account"
actual_text = driver.find_element(By. XPATH, "//h1[contains(@class, 'styles__StyledHeading')]").text
assert expected_text == actual_text, f"Expected {expected_text} but got. {actual_text}"

# SignIn button is shown
# (you can just use driver.find_element() to check for element’s presence, no need to assert here)
driver.find_element(By. ID, "login")
sleep(10)

