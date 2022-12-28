import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome")


@pytest.fixture(scope="class")
def setup(request):
    browser_name=request.config.getoption("browser_name")
    if browser_name=="chrome":
        service_obj = Service("C:/Users/saksh/Desktop/IDE SOFTWARES/chromedriver_win32/chromedriver.exe")
        driver = webdriver.Chrome(service=service_obj)
    elif browser_name=="firefox":
        print("firefox")
    elif browser_name =="ie":
        print("ie")
    driver.maximize_window()
    ## Navigating to Site ###
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.implicitly_wait(5)
    request.cls.driver = driver
    yield
    driver.close()
