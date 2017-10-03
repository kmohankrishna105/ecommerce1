from selenium import webdriver
import unittest
import time
from Ecommercepractice.Browserstart import chromeopen
from Ecommercepractice.Pages.SearchPage import Home
from Ecommercepractice.Pages.Checkout import Checkout
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

class ecommerce(chromeopen,unittest.TestCase):

    def testName(self):

        print("testName-Function")
        #print("inheritence accepted")
        "Home page object created"
        home=Home(self.driver)
        home.Enterstring("Samsung")
        home.ClickSearch()


        self.driver.find_element_by_xpath("//div[@class='row']//div[3]//div[@class='button-group']//i[@class='fa fa-shopping-cart']").click()
        "Cart page"
        self.driver.implicitly_wait(10)
        #self.driver.maximize_window()

        self.driver.find_element_by_xpath("//span[text()='Shopping Cart']").click()
        self.driver.implicitly_wait(10)
        self.driver.save_screenshot("D:/shopping.png")

        r=self.driver.find_element_by_xpath("//td[@class='text-right']")
        print (r)
        print(r.text)
        #print (f)

        self.driver.find_element_by_xpath("//span[text()='Checkout']").click()

        WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH, "//input[@value='guest']")))
        #WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.driver.find_element_by_xpath("//input[@value='guest']")))

        print ("Ec passed")
        "check out page"
        self.driver.implicitly_wait(10)
        member=Checkout(self.driver)
        member.Newmember()
        self.driver.save_screenshot("D:/hai.png")
        #self.driver.find_element_by_xpath("//span[text()='Shopping Cart']").click()


if __name__=="__main__":
    unittest.main()

"""
"multiple function names and testname, testname1 then whch one will be executed"

"How to return inner text or available content from a page"

"how to work on select options"


"how to extract all mandatory fields"
pull out all the  inner text for class with - "//div[contains(@class,'required']"



"""