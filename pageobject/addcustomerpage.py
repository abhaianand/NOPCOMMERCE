

from lib2to3.pgen2 import driver
from msilib.schema import Class
from select import Select
import time
from selenium.webdriver.support.ui import Select
import random
import string



class AddCustomers:
   link_customers_main_menu_xpath = "//div [@class = 'os-content']//nav [@class = 'mt-2']//li [@class = 'nav-item has-treeview menu-open']//i [@class = 'right fas fa-angle-left']"
   link_customers_submenu_xpath = "//body/div[3]/aside[1]/div[1]/div[4]/div[1]/div[1]/nav[1]/ul[1]/li[4]/ul[1]/li[1]/a[1]/i[1]"
   btn_addnew_xpath = "//body/div[3]/div[1]/form[1]/div[1]/div[1]/a[1]"
   txt_email_xpath = "//input[@id='Email']"
   txt_password_xpath = "//input[@id='Password']"
   txt_firstname_xpath = "//input[@id='FirstName']"
   txt_lastname_xpath = "//input[@id='LastName']"
   rdb_gender_male_id = "Gender_Male"
   rdm_gender_female_id = "Gender_Female"
   txt_DOB_id = "DateOfBirth"
   txt_company_name_id= "Company"
   lstitemAdministrators_xpath = "//li[contains(text(),'Administrators')]"
   chbox_is_tax_exempt_id ="IsTaxExempt"
   lstitemRegistered_xpath = "//li[contains(text(),'Registered')]"
   txt_newsletter_xpath ="//body/div[3]/div[1]/form[1]/section[1]/div[1]/div[1]/nop-cards[1]/nop-card[1]/div[1]/div[2]/div[9]/div[2]/div[1]/div[1]/div[1]/div[1]"
   txt_customer_roles_xpath = "//body/div[3]/div[1]/form[1]/section[1]/div[1]/div[1]/nop-cards[1]/nop-card[1]/div[1]/div[2]/div[10]/div[2]/div[1]/div[1]/div[1]/div[1]"
   drpdn_manager_of_vendor_id = "VendorId"

   lnkCustomers_menu_xpath = "//a[@href='#']//span[contains(text(),'Customers')]"
   lnkCustomers_menuitem_xpath = "//span[@class='menu-item-title'][contains(text(),'Customers')]"
   btnAddnew_xpath = "//a[@class='btn bg-blue']"
   txtEmail_xpath = "//input[@id='Email']"
   txtPassword_xpath = "//input[@id='Password']"
   txtcustomerRoles_xpath = "//div[@class='k-multiselect-wrap k-floatwrap']"
   lstitemAdministrators_xpath = "//li[contains(text(),'Administrators')]"
   lstitemRegistered_xpath = "//li[contains(text(),'Registered')]"
   lstitemGuests_xpath = "//li[contains(text(),'Guests')]"
   lstitemVendors_xpath = "//li[contains(text(),'Vendors')]"
   drpmgrOfVendor_xpath = "//*[@id='VendorId']"
   rdMaleGender_id = "Gender_Male"
   rdFeMaleGender_id = "Gender_Female"
   txtFirstName_xpath = "//input[@id='FirstName']"
   txtLastName_xpath = "//input[@id='LastName']"
   txtDob_xpath = "//input[@id='DateOfBirth']"
   txtCompanyName_xpath = "//input[@id='Company']"
   txtAdminContent_xpath = "//textarea[@id='AdminComment']"
   btnSave_xpath = "//button[@name='save']"


   def __init__(self,driver):
         self.driver = driver

   def click_customer_menu(self,):
      self.driver.find_element("xpath",self.link_customers_main_menu_xpath).click()

   def click_cutomers_submenu(self):
      self.driver.find_element("xpath",self.link_customers_submenu_xpath).click()

   def clickOnAddnew(self):
        self.driver.find_element("xpath",self.btn_addnew_xpath).click()

   def setEmail(self,email):
        self.driver.find_element("xpath",self.txt_email_xpath).send_keys(email)

   def setPassword(self,password):
        self.driver.find_element("xpath",self.txt_password_xpath).send_keys(password)  

   def setCustomerRoles(self,role):
        self.driver.find_elementh("xpath",self.txt_customer_roles_xpath).click()
        time.sleep(3)

        if role == 'Registered':
            self.listitem = self.driver.find_element("xpath",self.lstitemRegistered_xpath)
        elif role=='Administrators':

            self.listitem=self.driver.find_element("xpath",self.lstitemAdministrators_xpath)
        elif role=='Guests':

            # Here user can be Registered( or) Guest, only one
            time.sleep(3)
            self.driver.find_element_by_xpath("//*[@id='SelectedCustomerRoleIds_taglist']/li/span[2]").click()
            self.listitem = self.driver.find_element_by_xpath(self.lstitemGuests_xpath)
        elif role=='Registered':
            self.listitem = self.driver.find_element_by_xpath(self.lstitemRegistered_xpath)
        elif role=='Vendors':
            self.listitem = self.driver.find_element_by_xpath(self.lstitemVendors_xpath)
        else:
            self.listitem = self.driver.find_element_by_xpath(self.lstitemGuests_xpath)
        time.sleep(3)
        #self.listitem.click()
        self.driver.execute_script("arguments[0].click();", self.listitem)

   def setManagerOfVendor(self,value):
        drp=Select(self.driver.find_element_by_xpath(self.drpmgrOfVendor_xpath))
        drp.select_by_visible_text(value)

   def setGender(self,gender):
        if gender=='Male':
            self.driver.find_element_by_id(self.rdMaleGender_id).click()
        elif gender=='Female':
            self.driver.find_element_by_id(self.rdFeMaleGender_id).click()
        else:
            self.driver.find_element_by_id(self.rdMaleGender_id).click()

   def setFirstName(self, fname):
        self.driver.find_element_by_xpath(self.txtFirstName_xpath).send_keys(fname)

   def setLastName(self, lname):
        self.driver.find_element_by_xpath(self.txtLastName_xpath).send_keys(lname)

   def setDob(self, dob):
        self.driver.find_element("xpath",self.txtDob_xpath).send_keys(dob)

   def setCompanyName(self, comname):
        self.driver.find_element("xpath",self.txtCompanyName_xpath).send_keys(comname)

   def setAdminContent(self, content):
        self.driver.find_element("xpath",self.txtAdminContent_xpath).send_keys(content)

   def clickOnSave(self):
        self.driver.find_element("xpath",self.btnSave_xpath).click() 

   

   


 

