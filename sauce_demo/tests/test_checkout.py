from dbm import error

import pytest
import selenium

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from sauce_demo.utils.unltis import update_test_result


@pytest.fixture

def driver():
    """Khởi tạo và đóng trình duyệt Chrome"""
    service = selenium.webdriver.chrome.service.Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.NAME, "user-name").send_keys("standard_user")
    driver.find_element(By.NAME, "password").send_keys("secret_sauce")
    driver.find_element(By.NAME, "login-button").click()
    driver.find_element(By.NAME, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a').click()
    time.sleep(2)
    driver.find_element(By.NAME, "checkout").click()

    yield driver
    driver.quit()

def test_checkout_vaild(driver):
    test_name="test_checkout_vaild"
    try:
        driver.find_element(By.ID,"first-name").send_keys("lili")
        driver.find_element(By.ID,"last-name").send_keys("Brow")
        driver.find_element(By.ID,"postal-code").send_keys("111")
        driver.find_element(By.ID, "continue").click()
        time.sleep(2)
        driver.find_element(By.ID, "finish").click()
        assert driver.current_url.startswith("https://www.saucedemo.com/checkout-complete.html")
        update_test_result(test_name, 1, "Passed")
    except Exception as e:
        update_test_result(test_name, 5, "Failed")
        raise e

def test_checkout_blank_information(driver):
    test_name="test_checkout_blank_information"
    try:
        driver.find_element(By.ID, "continue").click()
        error_mgs = driver.find_element(By.XPATH, "//h3[@data-test='error']")
        assert 'Error: First Name is required' in error_mgs.text
        update_test_result(test_name, 1, "Passed")
    except Exception as e:
        update_test_result(test_name, 5, "Failed")
        raise e

def test_checkout_cancel(driver):
    test_name="test_checkout_cancel"
    try:
        driver.find_element(By.ID,"first-name").send_keys("Lili")
        driver.find_element(By.ID,"last-name").send_keys("Brow")
        driver.find_element(By.ID,"postal-code").send_keys("111")
        driver.find_element(By.ID, "continue").click()
        time.sleep(2)
        driver.find_element(By.ID, "cancel").click()
        assert driver.current_url.startswith("https://www.saucedemo.com/inventory.html")
        update_test_result(test_name, 1, "Passed")
    except Exception as e:
        update_test_result(test_name, 5, "Failed")
        raise e

