# import time
#
# from selenium.webdriver.chrome.service import Service
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions
# from selenium.webdriver.support.wait import WebDriverWait

from PythonFramework.pageObjects.CheckOutPage import *
from PythonFramework.pageObjects.HomePage import HomePage
from PythonFramework.utilities.BaseClass import BaseClass


class Test(BaseClass):
    def test_e2e(self):
        log = self.getLogger()
        homePage = HomePage(self.driver)
        # self.driver.find_element(By.LINK_TEXT, "Shop").click()
        checkoutPage = homePage.shopItems()
        log.info("getting card titles")
        web_products = []
        # text_grabbed = self.driver.find_elements(By.XPATH, "//div[@class='card h-100']")
        # checkoutPage = CheckOutPage(self.driver)
        text_grabbed = checkoutPage.getCardTitles()
        for element in text_grabbed:
            productsName = element.find_element(By.XPATH, "div/h4/a").text
            web_products.append(productsName)
            if productsName == "iphone X":
                # element.find_element(By.XPATH, "div/button").click()
                checkout = AddtoCart(element)
                checkout.getAddCart().click()
        log.warning(web_products)
        # self.driver.find_element(By.CSS_SELECTOR, ".nav-link.btn.btn-primary").click()
        # checkoutPage.getcheckoutButton().click()
        # time.sleep(5)
        # self.driver.find_element(By.CSS_SELECTOR, ".btn.btn-success").click()
        # checkoutPage.getConfirmCheckoutButton().click()
        confirmPage = checkoutPage.getcheckoutButton()
        log.warning("Entering country name")
        self.driver.find_element(By.CSS_SELECTOR, "#country").send_keys("ind")
        # wait = WebDriverWait(self.driver, 10)
        # wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
        self.explictWait("India")
        self.driver.find_element(By.LINK_TEXT, "India").click()
        log.warning("country name selected")
        # confirmPage.getSelect().click()
        # self.driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
        self.driver.find_element(By.CSS_SELECTOR, ".btn.btn-success.btn-lg").click()
        # confirm=confirmPage.getSelect()
        success = self.driver.find_element(By.CSS_SELECTOR, ".alert.alert-success.alert-dismissible").text
        assert "Success" in success
