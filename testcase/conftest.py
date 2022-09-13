from cgitb import html
from lib2to3.pgen2 import driver
from multiprocessing import managers
from webbrowser import Chrome
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
import pytest

@pytest.fixture()
def setup(browser):
   if browser == "Chrome":
    driver = webdriver.Chrome(executable_path="C:\\ABHAI\VS CODE\\chrome driver\\chromedriver.exe")
    print("starting chrome browser.........")
   elif browser == "firefox":
    driver = webdriver.Firefox(executable_path="C:\\ABHAI\VS CODE\\geckodriver-v0.31.0-win64\\geckodriver.exe")
    print("starting firfox...........") 
   return driver

  
def pytest_addoption(parser):   # this will get the value from cmd
   parser.addoption("--browser")

@pytest.fixture() 
def browser (request):   #this will return the browser to the method
   return request.config.getoption("--browser")   

############################pytest html report #########################
##add environment to report (hook) ###
def pytest_configure(config):
   config._metadata["project name "] = "nop commerce"
   config._metadata["module name "] = "customer"
   config._metadata["tester"] = "abhai"

#remove unwanted things(hook) from html report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
   metadata.pop("JAVA_HOME",None)
   metadata.pop("Plugins",None)   



    