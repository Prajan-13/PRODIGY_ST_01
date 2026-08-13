from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

# Start Chrome
options = Options()
driver = webdriver.Chrome(options=options)

try:
    # Open SauceDemo
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()

    # Login
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # Verify login
    assert "inventory" in driver.current_url
    print("Login successful")

    # Add product to cart
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    print("Product added to cart")

    # Open cart
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    # Verify cart page
    assert "cart" in driver.current_url
    print("Cart page opened")

    # Checkout
    driver.find_element(By.ID, "checkout").click()

    # Fill checkout information
    driver.find_element(By.ID, "first-name").send_keys("Prajan")
    driver.find_element(By.ID, "last-name").send_keys("Test")
    driver.find_element(By.ID, "postal-code").send_keys("600001")

    print("Checkout form filled")

    # Continue
    driver.find_element(By.ID, "continue").click()

    # Verify checkout overview
    assert "checkout-step-two" in driver.current_url
    print("Checkout overview displayed")

    # Finish purchase
    driver.find_element(By.ID, "finish").click()

    # Verify success message
    success_message = driver.find_element(
        By.CLASS_NAME, "complete-header"
    ).text

    assert success_message == "Thank you for your order!"

    print("Purchase completed successfully")
    print("SUCCESS MESSAGE:", success_message)

finally:
    time.sleep(2)
    driver.quit()
