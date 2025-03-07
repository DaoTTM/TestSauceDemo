import pytest
import selenium
import webdriver_manager
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

    yield driver
    driver.quit()


def test_login_vaild(driver):
    test_name = "test_login_valid"
    try:
        driver.find_element(By.NAME, "user-name").send_keys("standard_user")
        driver.find_element(By.NAME, "password").send_keys("secret_sauce")
        driver.find_element(By.NAME, "login-button").click()

        assert "inventory.html" in driver.current_url
        update_test_result(test_name, 1, "Test Passed")
    except Exception as e:
        update_test_result(test_name, 5, f"Test Failed: {str(e)}")
        raise e


def test_login_username_locked(driver):
    test_name = "test_login_username_locked"
    try:
        driver.find_element(By.NAME, "user-name").send_keys("locked_out_user")
        driver.find_element(By.NAME, "password").send_keys("secret_sauce")
        driver.find_element(By.NAME, "login-button").click()
        error_mgs = driver.find_element(By.XPATH, "//h3[@data-test='error']")
        assert "Epic sadface: Sorry, this user has been locked out." in error_mgs.text
        update_test_result(test_name, 1, "Test Passed")
    except Exception as e:
        update_test_result(test_name, 5, f"Test Failed: {str(e)}")
        raise e

def test_username_not_exist(driver):
    test_name = "test_username_not_exist"
    try:
        driver.find_element(By.NAME, "user-name").send_keys("notexist_user")
        driver.find_element(By.NAME, "password").send_keys("secret_sauce")
        driver.find_element(By.NAME, "login-button").click()
        error_mgs = driver.find_element(By.XPATH, "//h3[@data-test='error']")
        assert "Epic sadface: Username and password do not match any user in this service" in error_mgs.text
        update_test_result(test_name, 1, "Test Passed")
    except Exception as e:
        update_test_result(test_name, 5, f"Test Failed: {str(e)}")
        raise e

def test_password_wrong(driver):
    test_name = "test_password_wrong"
    try:
        driver.find_element(By.NAME, "user-name").send_keys("standard_user")
        driver.find_element(By.NAME, "password").send_keys("wrong_password")
        driver.find_element(By.NAME, "login-button").click()
        error_mgs = driver.find_element(By.XPATH, "//h3[@data-test='error']")
        assert "Epic sadface: Username and password do not match any user in this service" in error_mgs.text
        update_test_result(test_name, 1, "Test Passed")
    except Exception as e:
        update_test_result(test_name, 5, f"Test Failed: {str(e)}")
        raise e


def test_blank_username(driver):
    test_name = "test_blank_username"
    try:
        # driver.find_element(By.NAME, "user-name").send_keys("standard_user")
        driver.find_element(By.NAME, "password").send_keys("secret_sauce")
        driver.find_element(By.NAME, "login-button").click()
        error_mgs = driver.find_element(By.XPATH, "//h3[@data-test='error']")
        assert "Epic sadface: Username is required" in error_mgs.text
        update_test_result(test_name, 1, "Test Passed")
    except Exception as e:
        update_test_result(test_name, 5, f"Test Failed: {str(e)}")
        raise e

def test_blank_password(driver):
    test_name = "test_blank_password"
    try:
        driver.find_element(By.NAME, "user-name").send_keys("standard_user")
        # driver.find_element(By.NAME, "password").send_keys("secret_sauce")
        driver.find_element(By.NAME, "login-button").click()
        error_mgs = driver.find_element(By.XPATH, "//h3[@data-test='error']")
        assert "Epic sadface: Password is required" in error_mgs.text
        update_test_result(test_name, 1, "Test Passed")
    except Exception as e:
        update_test_result(test_name, 5, f"Test Failed: {str(e)}")
        raise e

def test_blank_all(driver):
    test_name = "test_blank_all"
    try:
        driver.find_element(By.NAME, "login-button").click()
        error_mgs = driver.find_element(By.XPATH, "//h3[@data-test='error']")
        assert "Epic sadface: Username is required" in error_mgs.text
        update_test_result(test_name, 1, "Test Passed")
    except Exception as e:
        update_test_result(test_name, 5, f"Test Failed: {str(e)}")
        raise e

