import time

from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

obj = Service("C:/Users/malatk/Downloads/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=obj)
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
driver.find_element(By.LINK_TEXT, "Shop").click()
web_products = []
text_grabbed = driver.find_elements(By.XPATH, "//div[@class='card h-100']")
for element in text_grabbed:
    productsName = element.find_element(By.XPATH, "div/h4/a").text
    web_products.append(productsName)
    if productsName == "iphone X":
        element.find_element(By.XPATH, "div/button").click()
driver.find_element(By.CSS_SELECTOR, ".nav-link.btn.btn-primary").click()
time.sleep(5)
driver.find_element(By.CSS_SELECTOR, ".btn.btn-success").click()

driver.find_element(By.CSS_SELECTOR, "#country").send_keys("ind")
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT,"India")))
driver.find_element(By.LINK_TEXT,"India").click()
driver.find_element(By.XPATH,"//div[@class='checkbox checkbox-primary']").click()
driver.find_element(By.CSS_SELECTOR,".btn.btn-success.btn-lg").click()
success=driver.find_element(By.CSS_SELECTOR,".alert.alert-success.alert-dismissible").text
assert "Success" in success