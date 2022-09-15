from lib2to3.pgen2 import driver
from selenium import webdriver
import pytest
from pageobject.loginpage import Login
from datetime import datetime
from testcase.conftest import setup
from utilities.readproperties import Readconfig 
from utilities.customlogger import Logger
from utilities import xlutils
import time

class Test_case_id_ddt_001:
    base_url=Readconfig.getapplicationURL()
    path = ".//testdata/testdatafile.xlsx"
    now = datetime.now().strftime("%Y-%m-%d_%H%M%S")

    Logger1 = Logger.loggen()
    
    @pytest.mark.regression

    def test_login_ddt(self,setup):
        self.Logger1.info("****************Test_001_Login_ddt**********************")
        self.driver = setup
        self.driver.get(self.base_url)
        self.lp=Login(self.driver)
        self.rows = xlutils.getRawCount(self.path,'testdata')
        print("number of rows",self.rows) 

        lst_status = []  #empty list varaible

        for r in range(2,self.rows+1):
            self.user_name = xlutils.ReadData(self.path,'testdata',r,1)
            self.password = xlutils.ReadData(self.path,'testdata',r,2)
            self.exp_result = xlutils.ReadData(self.path,'testdata',r,3)

            self.lp.setusername(self.user_name)
            self.lp.setpassword(self.password)
            self.lp.clicklogin()
            time.sleep(3)

            actual_title = self.driver.title
            expected_title = "Dashboard / nopCommerce administration"

            if actual_title == expected_title:
                if self.exp_result == "pass":
                    self.Logger1.info("******passed*****")
                    self.lp.clicklogout() 
                    time.sleep(2)
                    lst_status.append("pass")
                elif self.exp_result == "fail":
                     self.Logger1.info("*****fail*******")
                     self.lp.clicklogout()
                     time.sleep(2)
                     lst_status.append("fail")
            elif actual_title != expected_title:
                if self.exp_result == "pass":
                    self.Logger1.info("******fail******")
                    self.lp.clicklogout()
                    lst_status.append("fail")
                elif self.exp_result =="fail":
                     self.Logger1.info("***pass***")         
                     lst_status.append("****pass****")  #jhjh
        if "fail" not in lst_status:
            self.Logger1.info("***ddt test pass****")
            self.driver.close()
            assert True
        else:
            self.Logger1.info("******ddt test failed****")  
            self.driver.close()
            assert False









      



        
