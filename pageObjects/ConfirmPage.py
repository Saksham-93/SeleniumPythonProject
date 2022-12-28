from selenium.webdriver.common.by import By

class ConfirmPage:

    def __init__(self,driver):
        self.driver = driver

    countryDropDown = (By.ID, "country")
    selectCountry  = (By.LINK_TEXT, "India")
    countryName = (By.ID, "country")
    termsCheckBox = (By.CSS_SELECTOR, ".checkbox.checkbox-primary")
    purchaseButton = (By.XPATH, "//*[@value='Purchase']")
    successMessage = (By.CSS_SELECTOR, "div.alert-success")

    def getCountryDropDown(self):
        return self.driver.find_element(*ConfirmPage.countryDropDown)

    def clickCountry(self):
        return self.driver.find_element(*ConfirmPage.selectCountry)

    def getcountryName(self):
        return self.driver.find_element(*ConfirmPage.countryName)

    def clickTermsCheckBox(self):
        return self.driver.find_element(*ConfirmPage.termsCheckBox)

    def clickPurchaseButton(self):
        return self.driver.find_element(*ConfirmPage.purchaseButton)

    def getSuccessMessage(self):
        return self.driver.find_element(*ConfirmPage.successMessage)

