from selenium.webdriver.common.by import By

from PythonFramework.pageObjects.CheckOutPage import CheckOutPage


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    # self.driver.find_element(By.LINK_TEXT, "Shop").click()

    shop = (By.LINK_TEXT, "Shop")

    def shopItems(self):
        self.driver.find_element(*HomePage.shop).click()
        checkoutPage = CheckOutPage(self.driver)
        return checkoutPage
