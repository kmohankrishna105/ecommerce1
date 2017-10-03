from selenium import webdriver
import unittest
import time

class ecommerce(unittest.TestCase):


    def setUp(self):
        print("setup")
        cdrive = "C:/Python34/chromedriver.exe"
        self.driver = webdriver.Chrome(cdrive)
        self.driver.get("http://shop.thetestingworld.com/index.php?route=common/home")
        self.driver.maximize_window()

    #def tearDown(self):
        #print("Tear down")

    def testName(self):
        print("test")
        "search page"
        self.driver.find_element_by_xpath("//input[@name='search']").send_keys("samsung")
        self.driver.find_element_by_css_selector("i.fa.fa-search").click()
        self.driver.find_element_by_xpath("//div[@class='row']//div[3]//div[@class='button-group']//i[@class='fa fa-shopping-cart']").click()
        "Cart page"
        self.driver.implicitly_wait(10)
        #self.driver.maximize_window()

        self.driver.find_element_by_xpath("//span[text()='Shopping Cart']").click()
        self.driver.implicitly_wait(10)
        r=self.driver.find_element_by_xpath("//td[@class='text-right']")
        print (r)
        print(r.text)
        #print (f)

        self.driver.find_element_by_xpath("//span[text()='Checkout']").click()
        "check out page"
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_css_selector("input[value='guest']").click()
        self.driver.find_element_by_xpath("//input[@value='Continue']").click()
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_id("input-payment-firstname").send_keys("FirstName")
        self.driver.find_element_by_id("input-payment-lastname").send_keys("LastName")
        self.driver.find_element_by_id("input-payment-email").send_keys("Email")
        self.driver.save_screenshot("D:/Checkout.png")

        #self.driver.find_element_by_xpath("//span[text()='Shopping Cart']").click()


if __name__=="__main__":
    unittest.main()


"multiple function names and testname, testname1 then whch one will be executed"
"How to return inner text or available content from a page"

"how to work on select options"