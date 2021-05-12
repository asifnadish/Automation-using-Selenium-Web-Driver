# python download_image.py
import time
import urllib.request
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

sitem = input("enter the search item :")
sitem = sitem.split()
sitem = '+'.join(sitem)
driver=webdriver.Chrome(executable_path=r'C:\python\Lib\site-packages\selenium\webdriver\chrome\chromedriver.exe')

driver.get("https://www.google.com/search?q="+sitem+"+picture&rlz=1C1CHBD_enIN784IN784&source=lnms&tbm=isch&sa=X&ved=0ahUKEwi57e7FosXjAhUFTI8KHSm-BHwQ_AUIEigC&biw=1023&bih=657")
driver.maximize_window()
lists = driver.find_elements_by_tag_name("img")
lists.pop(0)
lists.pop(0)
#lists.pop(1)
i=1
for listitem in lists:
   var = listitem.get_attribute('src')
   urllib.request.urlretrieve(var, 'img'+str(i)+'.png' )
   
   i=i+1
   if(i>=11):
      break
print(str(i-1)+" images downloaded")
time.sleep(8)

driver.close()