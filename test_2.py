import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from login_page import Login_page


class Test_2():

    def test_select_product(self):
        driver = webdriver.Chrome()
        base_url = 'https://www.saucedemo.com'
        driver.get(base_url)
        driver.maximize_window()
        time.sleep(2)

        print("Start Test")

        login_problem_user = 'problem_user'
        password_all = 'secret_sauce'

        login = Login_page(driver)
        login.authorization(login_problem_user, password_all)

        select_product = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//button[@id="add-to-cart-sauce-labs-backpack"]')))
        select_product.click()
        print('Click Select Product')

        enter_shopping_cart = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//div[@id="shopping_cart_container"]')))
        enter_shopping_cart.click()
        print('Click Enter Shopping Cart')

        success_test = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//span[@class="title"]')))
        value_success_test = success_test.text
        print(value_success_test)
        assert value_success_test == "YOUR CART"
        print('Test Success')


test = Test_2()
test.test_select_product()