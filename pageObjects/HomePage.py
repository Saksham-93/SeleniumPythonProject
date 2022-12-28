from selenium.webdriver.common.by import By

from pageObjects.CheckOutPage import CheckOutPage


class HomePage:

    def __init__(self,driver):
        self.driver = driver

    shop = (By.XPATH, "//a[text()='Shop']")
    name = (By.XPATH,"(//*[@name='name'])[1]")
    email = (By.XPATH,"//*[@name='email']")
    iceCreamCheckBox = (By.ID,"exampleCheck1")
    selectGender = (By.ID,"exampleFormControlSelect1")
    submitButton = (By.XPATH,"//*[@value='Submit']")
    successMessage = (By.CSS_SELECTOR,".alert.alert-success.alert-dismissible")

    def shopItems(self):
        self.driver.find_element(*HomePage.shop).click()
        checkoutpage = CheckOutPage(self.driver)
        return checkoutpage

    def getName(self):
        return self.driver.find_element(*HomePage.name)

    def getEmail(self):
        return self.driver.find_element(*HomePage.email)

    def clickIceCreamCheckBox(self):
        return self.driver.find_element(*HomePage.iceCreamCheckBox)

    def getGender(self):
        return self.driver.find_element(*HomePage.selectGender)

    def getSuccessMessage(self):
        return self.driver.find_element(*HomePage.successMessage)

    def clickSubmitButton(self):
        return self.driver.find_element(*HomePage.submitButton)

