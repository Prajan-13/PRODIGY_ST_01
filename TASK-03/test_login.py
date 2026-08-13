from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_login():
    driver = webdriver.Chrome()

    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    time.sleep(2)

    assert "inventory.html" in driver.current_url

    driver.quit()
