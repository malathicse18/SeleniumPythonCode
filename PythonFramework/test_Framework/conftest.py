import pytest
from selenium.webdriver.chrome.service import Service
from selenium import webdriver


# def pytest_addoption(parser):
#     parser.addoption("--browser_name", action="store", default="chrome")
#
#
# @pytest.fixture(scope="class")
# def setup(request):
#
#     browser_name = request.config.getoption("--browser_name")
#     if browser_name == "chrome":
#         obj = Service("C:/Users/malatk/Downloads/chromedriver-win64/chromedriver.exe")
#         driver = webdriver.Chrome(service=obj)
#         driver.implicitly_wait(5)
#         driver.get("https://rahulshettyacademy.com/angularpractice/")
#         driver.maximize_window()
#         request.cls.driver = driver
#         yield
#         driver.close()
#     elif browser_name == "firefox":
#         pass
#     elif browser_name == "IE":
#         pass
# Add this to your pytest_addoption function

@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption("--browser_name")
    driver = None  # Initialize driver as None

    if browser_name == "chrome":
        obj = Service("C:/Users/malatk/Downloads/chromedriver-win64/chromedriver.exe")
        driver = webdriver.Chrome(service=obj)
    elif browser_name == "firefox":
        # Add Firefox driver setup logic here
        pass
    elif browser_name == "IE":
        # Add IE driver setup logic here
        pass
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")

    if driver:
        driver.implicitly_wait(5)
        driver.maximize_window()
        driver.get("https://rahulshettyacademy.com/angularpractice/")
        request.cls.driver = driver

    yield driver

    if driver:
        driver.close()


# Add this to your pytest_addoption function
def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome")