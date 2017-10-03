from selenium import webdriver

"how to extract all mandatory fields text"

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

cdrive = "C:/Python34/chromedriver.exe"
driver=webdriver.Chrome(cdrive)
driver.get("http://shop.thetestingworld.com/index.php?route=common/home")
driver.maximize_window()
driver.find_element_by_xpath("//input[@name='search']").send_keys("samsung")
driver.find_element_by_css_selector("i.fa.fa-search").click()
driver.implicitly_wait(5)
driver.find_element_by_xpath("//div[@class='row']//div[3]//div[@class='button-group']//i[@class='fa fa-shopping-cart']").click()
driver.implicitly_wait(10)
driver.find_element_by_xpath("//span[text()='Checkout']").click()
print("checkout selected")
driver.implicitly_wait(40)
WebDriverWait(driver,40).until(EC.element_to_be_clickable((By.XPATH,"//input[@value='guest']")))
driver.find_element_by_xpath("//input[@value='guest']").click()
driver.implicitly_wait(30)

driver.find_element_by_xpath("//input[@value='Continue']").click()
driver.implicitly_wait(20)
list=[]

list=driver.find_elements_by_xpath("//div[contains(@class,'e')]")

#list=driver.find_elements_by_xpath("//div[contains(@class,'required')]")
print (list)
for n in list:
    print(n.text)
    print(n.get_attribute("class"))
#==================================================================================================================================



