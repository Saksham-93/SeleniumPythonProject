from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import pytest

from pageObjects.CheckOutPage import CheckOutPage
from pageObjects.ConfirmPage import ConfirmPage
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_e2e(self):
        log = self.test_loggerDemo()
        ## Click on the Shop Button ##
        homepage = HomePage(self.driver)
        checkoutpage = homepage.shopItems()
        log.info("Click on the Shop Tab")
        ## Working with Products List ##

        productList = checkoutpage.getProductList()
        log.info("To get the Products List")
        productNameToSelect = "Blackberry"

        for products in productList:
            productName = products.find_element(By.XPATH, "h4/a").text
            if productName == productNameToSelect:
                products.find_element(By.XPATH, "following::button").click()

        ## Clicking on the CheckOut Button
        checkoutpage.getCheckOutButton().click()
        verifyProductName = checkoutpage.getVerifyProductName().text
        assert productNameToSelect == verifyProductName

        ## Click on Second CheckOut Button
        confirmpage = checkoutpage.getSuccessCheckoutButton()

        ## Handling Dynamic DropDown

        confirmpage.getCountryDropDown().send_keys("ind")
        self.verifyLinkPresence("India")
        confirmpage.clickCountry().click()

        countryName = confirmpage.getcountryName().get_attribute("value")
        log.info("The Country name is" + countryName)
        assert "India" == countryName

        ## Click on the CheckBox
        confirmpage.clickTermsCheckBox().click()

        ## Click on the Purchase Button

        confirmpage.clickPurchaseButton().click()

        ## Validating the SuccessMessage

        successMessage = confirmpage.getSuccessMessage().text
        log.info("Success Message is" + successMessage)

        assert "Success" in successMessage
