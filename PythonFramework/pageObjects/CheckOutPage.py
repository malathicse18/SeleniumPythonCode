from selenium.webdriver.common.by import By

from PythonFramework.pageObjects.ConfirmPage import ConfirmPage


class CheckOutPage:
    def __init__(self, driver):
        self.driver = driver

    # text_grabbed= self.driver.find_elements(By.XPATH, "//div[@class='card h-100']")
    cardTitle = (By.XPATH, "//div[@class='card h-100']")
    # self.driver.find_element(By.CSS_SELECTOR, ".nav-link.btn.btn-primary").click()
    checkoutbtn = (By.CSS_SELECTOR, ".nav-link.btn.btn-primary")
    # self.driver.find_element(By.CSS_SELECTOR, ".btn.btn-success").click()
    confirmCheckout = (By.CSS_SELECTOR, ".btn.btn-success")

    def getCardTitles(self):
        return self.driver.find_elements(*CheckOutPage.cardTitle)

    def getcheckoutButton(self):
        self.driver.find_element(*CheckOutPage.checkoutbtn).click()
        self.driver.find_element(*CheckOutPage.confirmCheckout).click()
        confirmPage = ConfirmPage(self.driver)
        return confirmPage


class AddtoCart:
    def __init__(self, element):
        self.element = element

    # element.find_element(By.XPATH, "div/button").click()
    addCart = (By.XPATH, "div/button")

    def getAddCart(self):
        return self.element.find_element(*AddtoCart.addCart)
