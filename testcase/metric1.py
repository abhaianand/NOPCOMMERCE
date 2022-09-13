from selenium import webdriver
import time
import random
import string


driver = webdriver.Chrome(executable_path="C:\\ABHAI\VS CODE\\chrome driver\\chromedriver.exe")
driver.maximize_window()
driver.get("https://metrictreelabs.com/")
time.sleep(1)

for _ in range(5):
  def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
     return ''.join(random.choice(chars) for x in range(size))
  driver.find_element("name","your-name").send_keys("demo1")
  email = random_generator() + "@gmail.com"
  driver.find_element("name","your-email").send_keys(email)
  driver.find_element("name","phone").send_keys("9567231866")
  driver.find_element("name","message").send_keys("dont worry its just demo")
   #driver.find_element("xpath","//body/div[@id='Wrapper']/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/form[1]/p[1]/input[1]").click()
  time.sleep(1)
  driver.refresh()

