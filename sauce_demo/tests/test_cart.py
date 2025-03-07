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
    driver.find_element(By.NAME, "user-name").send_keys("standard_user")
    driver.find_element(By.NAME, "password").send_keys("secret_sauce")
    driver.find_element(By.NAME, "login-button").click()

    yield driver

    driver.quit()


def test_addproduct_success(driver):
    test_name="test_addproduct_success"
    try:
        expected_count = 1
        driver.find_element(By.NAME,"add-to-cart-sauce-labs-backpack").click()
        cart_badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
        assert int(cart_badge) == expected_count
        update_test_result(test_name, 1, "Test Passed")
    except Exception as e:
        update_test_result(test_name, 5, f"Test Failed:{str(e)}")
        raise e

def test_remove_cart(driver):
    test_name="test_remove_card"
    try:
        # expected_count = 0
        driver.find_element(By.NAME,"add-to-cart-sauce-labs-backpack").click()
        driver.find_element(By.NAME,"remove-sauce-labs-backpack").click()
        add_product_to_cart = driver.find_element(By.NAME,"add-to-cart-sauce-labs-backpack")
        assert add_product_to_cart.is_displayed()
        update_test_result(test_name, 1, "Test Passed")
    except Exception as e:
        update_test_result(test_name, 5, f"Test Failed:{str(e)}")
        raise e

def test_checkout_from_cart(driver):
    test_name="test_checkout_from_cart"
    try:
        driver.find_element(By.NAME, "add-to-cart-sauce-labs-backpack").click()
        # driver.find_element(By.NAME, "remove-sauce-labs-backpack").click()
        driver.find_element(By.XPATH,'//*[@id="shopping_cart_container"]/a').click()
        time.sleep(5)
        driver.find_element(By.NAME,"checkout").click()

        assert driver.current_url.startswith ("https://www.saucedemo.com/checkout-step-one.html")
        update_test_result(test_name, 1, "Test Passed")

    except Exception as e:
        update_test_result(test_name, 5, "Test Failed")
        raise e