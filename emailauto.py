# python emailauto.py
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#create a chrome session
driver=webdriver.Chrome(executable_path=r'C:\python\Lib\site-packages\selenium\webdriver\chrome\chromedriver.exe')
driver.implicitly_wait(30)
driver.maximize_window()

#navigate to the application home page
driver.get("https://mail.google.com/mail/?tab=wm&ogb1")

user_field = driver.find_element_by_id("identifierId")
user_field.clear();

#enter email id and submit

user_field.send_keys("aasifnadish@gmail.com")
driver.find_element_by_id("identifierNext").click()

#password field
driver.find_element_by_name("password").send_keys("Iqbal35zaks")

driver.find_element_by_id("passwordNext").click()


#compose field
driver.find_element_by_css_selector("div.T-I.J-J5-Ji.T-I-KE.L3").click()

#sending to
#driver.find_element_by_css_selector("div#:9b.oL.aDm").click()

driver.find_element_by_class_name("vO").send_keys("aasifnadish@gmail.com")

#subject field
#driver.find_element_by_class_name("aot").click()
driver.find_element_by_class_name("aoT").send_keys("sending email using selenium web driver")

#body field
body_field = driver.find_element_by_class_name("Am.Al.editable.LW-avf")
body_field.send_keys("Automation testing is a Software testing technique to test and compare the actual outcome with the expected outcome. ")

# click on send button
driver.find_element_by_class_name("T-I.J-J5-Ji.aoO.v7.T-I-atl.L3").click()
print("email sent sucessfully")

time.sleep(10)
driver.close()











