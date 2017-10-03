from selenium import webdriver

"Open chromedriver and navigate to shopping site"
cdrive = "C:/Python34/chromedriver.exe"
driver=webdriver.Chrome(cdrive)
driver.get("http://shop.thetestingworld.com/index.php?route=common/home")

#asssert for the logo available ?
#assert("//img[@src='http://shop.thetestingworld.com/image/catalog/logo2.jpg']",)

driver.find_element_by_xpath("//input[@name='search']").send_keys("samsung")

driver.find_element_by_css_selector("i.fa.fa-search").click()



#how to verify the number of search elements in the web site?

#Page 2 element
driver.implicitly_wait(5)
#click on second similar logo available in page ?
#driver.find_element_by_xpath("//div[@class='row']//div[3]//div[@class='button-group']//i[@class='fa fa-shopping-cart']").click()
driver.find_element_by_xpath("//div[@class='row']//div[3]//div[@class='button-group']//i[@class='fa fa-shopping-cart']").click()

#assert success message for addition?


#driver.find_element_by_css_selector("span#cart-total").click()
driver.implicitly_wait(10)
driver.find_element_by_xpath("//span[text()='Checkout']").click()
driver.find_element_by_xpath("//span[text()='Shopping Cart']").click()


