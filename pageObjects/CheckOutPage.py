from selenium.webdriver.common.by import By

from pageObjects.ConfirmPage import ConfirmPage


class CheckOutPage:

    def __init__(self, driver):
        self.driver = driver

    cardBody = (By.XPATH, "//*[@class='card-body']")
    productText = (By.XPATH, "h4/a")
    clickAddButton = (By.XPATH, "following::button")
    checkOutButton = (By.XPATH, "//*[@id='navbarResponsive']//a")
    verifyProductname = (By.CSS_SELECTOR, "h4.media-heading a:nth-child(1)")
    successCheckOutButton = (By.CSS_SELECTOR, ".btn.btn-success")


    def getProductList(self):
        return self.driver.find_elements(*CheckOutPage.cardBody)

    def getProductName(self):
        return self.driver.find_element(*CheckOutPage.productText)

    def getclickAddButton(self):
        return self.driver.find_element(*CheckOutPage.clickAddButton)

    def getCheckOutButton(self):
        return self.driver.find_element(*CheckOutPage.checkOutButton)

    def getVerifyProductName(self):
        return self.driver.find_element(*CheckOutPage.verifyProductname)

    def getSuccessCheckoutButton(self):
        self.driver.find_element(*CheckOutPage.successCheckOutButton).click()
        confirmpage = ConfirmPage(self.driver)
        return confirmpage
