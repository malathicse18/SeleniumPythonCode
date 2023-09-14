from selenium.webdriver.common.by import By


class ConfirmPage:
    def __init__(self, driver):
        self.driver = driver

    # self.driver.find_element(By.LINK_TEXT, "India").click()

    dropDown = (By.LINK_TEXT, "india")
    # self.driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
    # checkBox = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
    # # self.driver.find_element(By.CSS_SELECTOR, ".btn.btn-success.btn-lg").click()
    # purchaseButton = (By.CSS_SELECTOR, ".btn.btn-success.btn-lg")

    def getSelect(self):
        return self.driver.find_element(*ConfirmPage.dropDown)
        # return self.driver.find_element(*ConfirmPage.checkBox)
        # return self.driver.find_element(*ConfirmPage.purchaseButton).click()
