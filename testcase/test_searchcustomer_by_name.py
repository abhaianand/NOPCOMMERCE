import pytest
import time
from pageobject.loginpage import Login
from testcase.conftest import setup
from utilities.readproperties import Readconfig
from utilities.customlogger import Logger
from pageobject.addcustomerpage import AddCustomers
from pageobject.SearchCustomerPage import Search_customer 

class Test_SearchCustomerByEmail_004:
    baseURL = Readconfig.getApplicationURL()
    username = Readconfig.getUsername()
    password = Readconfig.getPassword()
    logger1 = Logger.loggen()  # Logger

    @pytest.mark.regression
    def test_searchCustomerByEmail(self,setup):
        self.logger1.info("************* SearchCustomerByEmail_004 **********")
        self.driver=setup
        self.driver.get(self.base_url)
        self.driver.maximize_window()

        self.lp = Login(self.driver)
        self.lp.setusername(self.username)
        self.lp.setpassword(self.password)
        self.lp.clicklogin()
        self.logger1.info("************* Login succesful **********")

        self.logger1.info("******* Starting Search Customer By name **********")

        self.addcust = AddCustomers(self.driver)
        self.addcust.click_customer_menu()
        self.addcust.click_cutomers_submenu()

        self.logger1.info("************* searching customer by name **********")
        searchcust = Search_customer(self.driver)
        searchcust.setFirstName("Victoria")
        searchcust.setLastName("Terces")
        searchcust.clickSearch()
        time.sleep(5)
        status=searchcust.searchCustomerByName("Victoria Terces")
        self.driver.close()
        assert True==status
        self.logger1.info("***************  TC_SearchCustomerByName_005 Finished  ***********")
        self.driver.close()
