from pageobject.addcustomerpage import AddCustomers
from pageobject.loginpage import Login
import string
import random
import pytest



class Test_003_addcustomer:
    base_url=Readconfig.getapplicationURL()
    user_name=Readconfig.getUsername()
    password=Readconfig.getpassword()
    Logger1 = Logger.loggen()

    @pytest.mark.sanity

    def test_addcustomer(self,setup):
        self.Logger1.info("****************Test_001_Login**********************")
        self.driver = setup
        self.driver.get(self.base_url)
        self.lp=Login(self.driver)
        self.lp.setusername(self.user_name)
        self.lp.setpassword(self.password)
        self.lp.clicklogin()
        self.Logger1.info("***********login succesful*********")

        self.Logger1.info("********starting add customer **********")

        self.addcust = AddCustomers(self.driver)
        self.addcust.click_customer_menu()
        self.addcust.click_cutomers_submenu()
        self.addcust.clickOnAddnew()

        self.Logger1.info("*******providing customer info ************")
        self.email =  random_generator() + "@gmail.com"
        self.addcust.setEmail(self.email)
        self.addcust.setPassword("123456")
        self.addcust.setFirstName("abhai")
        self.addcust.setLastName("anand")
        self.addcust.setGender("male")
        self.addcust.setDob("4/01/1995")
        self.addcust.setCompanyName("MTL")
        self.addcust.setAdminContent("this is a demo test")
        self.addcust.clickOnSave()
        self.Logger1.info("***********saving customer info**********")
        self.Logger1.info("*******add customer validation started*************")

        self.msg = self.driver.find_element("xpath","body").text
        print(self.msg)
        if 'The new customer has been added successfully.' in self.msg:
            assert True == True
            self.Logger1.info("******************add customer test passed ******************")
        else :
            self.driver.save_screenshot(".\\screenshots\\"+"test_addCustomer_scr.png") # Screenshot
            self.Logger1.info("**************add customer test failed*****************")
            assert True == False

        self.driver.close()
        self.Logger1.info("*******************ending home page title test ********************")

def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
     return ''.join(random.choice(chars) for x in range(size))   
        





