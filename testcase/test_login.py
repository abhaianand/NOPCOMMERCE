from lib2to3.pgen2 import driver
from selenium import webdriver
import pytest
from pageobject.loginpage import Login
from datetime import datetime
from testcase.conftest import setup
from utilities.readproperties import Readconfig 
from utilities.customlogger import Logger

class Test_case_id_001:
    base_url=Readconfig.getapplicationURL()
    user_name=Readconfig.getUsername()
    password=Readconfig.getpassword()
    now = datetime.now().strftime("%Y-%m-%d_%H%M%S")

    Logger1 = Logger.loggen()
    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self,setup):
        self.Logger1.info("****************Test_001_Login**********************")
        self.driver = setup
        self.driver.get(self.base_url)
        self.lp=Login(self.driver)
        self.lp.setusername(self.user_name)
        self.lp.setpassword(self.password)
        self.lp.clicklogin()
        actual_title = self.driver.title
        if actual_title=="Dashboard / nopCommerce administration":
            assert True
            self.Logger1.info("****************passed**************")
            self.lp.clicklogout()
           
        else:
            self.driver.save_screenshot(".\\screenshots\\"+ self.now +"Test_case_id_001.png")
            self.Logger1.error("*************fail*******************")
            assert False
        self.lp.clicklogout()
          

      



        
