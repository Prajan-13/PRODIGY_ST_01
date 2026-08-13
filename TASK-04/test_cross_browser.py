import os
from selenium import webdriver
from selenium.webdriver.common.by import By


USERNAME = os.environ.get("BROWSERSTACK_USERNAME")
ACCESS_KEY = os.environ.get("BROWSERSTACK_ACCESS_KEY")

URL = "https://www.saucedemo.com"

browsers = [
    ("Chrome", "Windows", "11"),
    ("Firefox", "Windows", "11"),
    ("Edge", "Windows", "11"),
    ("Safari", "OS X", "Sonoma")
]


def test_login(browser, os_name, os_version):

    options = webdriver.ChromeOptions() if browser == "Chrome" else \
              webdriver.FirefoxOptions() if browser == "Firefox" else \
              webdriver.EdgeOptions() if browser == "Edge" else \
              webdriver.SafariOptions()

    options.browser_version = "latest"

    options.set_capability("bstack:options", {
        "os": os_name,
        "osVersion": os_version,
        "sessionName": f"SauceDemo Login - {browser}",
        "buildName": "Task-04 Cross Browser Testing"
    })

    driver = webdriver.Remote(
        command_executor=f"https://{USERNAME}:{ACCESS_KEY}@hub-cloud.browserstack.com/wd/hub",
        options=options
    )

    try:
        driver.get(URL)

        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        assert "inventory" in driver.current_url

        print(f"{browser}: LOGIN TEST PASSED")

        driver.execute_script(
            'browserstack_executor: {"action": "setSessionStatus",'
            ' "arguments": {"status":"passed","reason":"Login successful"}}'
        )

    except Exception as e:

        print(f"{browser}: LOGIN TEST FAILED - {e}")

        driver.execute_script(
            'browserstack_executor: {"action": "setSessionStatus",'
            ' "arguments": {"status":"failed","reason":"Login test failed"}}'
        )

        raise

    finally:
        driver.quit()


if __name__ == "__main__":

    if not USERNAME or not ACCESS_KEY:
        raise Exception(
            "Set BROWSERSTACK_USERNAME and BROWSERSTACK_ACCESS_KEY first."
        )

    for browser, os_name, os_version in browsers:
        test_login(browser, os_name, os_version)
