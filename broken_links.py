#  python broken_links.py
import requests
from selenium import webdriver


#create a chrome session
driver=webdriver.Chrome(executable_path=r'C:\python\Lib\site-packages\selenium\webdriver\chrome\chromedriver.exe')
driver.implicitly_wait(30)
driver.maximize_window()
#navigate to application home page 
driver.get("http://www.google.com")  					# website URL to which you want to check number of broken hyperlinks, i'am checking for "http://www.google.com" 
count=0;
links = driver.find_elements_by_css_selector("a")
for link in links:
	r = requests.head(link.get_attribute('href'))
	print("available links are : "+ link.get_attribute('href'),r.status_code)
	# print("links are" +link.get_attribute('href'), r.status_code)
	if (r.status_code >= 400):	
		count=count+1
print("total number of broken hyperlinks are : "+str(count))

driver.close();