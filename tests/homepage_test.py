from selenium.webdriver.support.select import Select

from TestData.HomePageData import HomePageData
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import pytest


class TestHomepage(BaseClass):

    def test_homepage(self,getData):
        homepage = HomePage(self.driver)
        homepage.getName().send_keys(getData["firstname"])
        homepage.getEmail().send_keys(getData["email"])
        homepage.clickIceCreamCheckBox().click()
        self.selectOptionsByText(homepage.getGender(),getData["gender"])
        homepage.clickSubmitButton().click()
        verifyText = homepage.getSuccessMessage().text
        assert "Success" in verifyText
        self.driver.refresh()

    @pytest.fixture(params=HomePageData.test_HomePage_data)
    def getData(self,request):
        return request.param

