from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class Login:
    textbox_username_xpath="//div[@class = 'inputs']//input[@name = 'Email']"
    textbox_password_xpath="//input[@id='Password']"
    loginbutton_xpath="//button[text()='Log in']"
    linktext_logout="//a[contains(text(),'Logout')]"

    def __init__(self,driver):
        self.driver=driver

    def setusername(self,username):
        self.driver.find_element("xpath",self.textbox_username_xpath).clear()
        self.driver.find_element("xpath",self.textbox_username_xpath).send_keys(username)


    def setpassword(self,password):
        self.driver.find_element("xpath",self.textbox_password_xpath).clear()
        self.driver.find_element("xpath",self.textbox_password_xpath).send_keys(password)

    def clicklogin(self):
        self.driver.find_element("xpath",self.loginbutton_xpath).click()

    def clicklogout(self):
        self.driver.find_element("xpath",self.linktext_logout).click()






