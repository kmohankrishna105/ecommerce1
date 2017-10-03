from selenium import webdriver
import unittest
import time

class chromeopen(unittest.TestCase):


    def setUp(self):
        print("chromeopen Inheritence-setup")
        cdrive = "C:/Python34/chromedriver.exe"
        self.driver = webdriver.Chrome(cdrive)
        self.driver.get("http://shop.thetestingworld.com/index.php?route=common/home")
        self.driver.maximize_window()

    def tearDown(self):
        self.testName_chromeopen()
        print("chromeopen Inheritence - Tear Down")

    def testName_chromeopen(self):
        print("chromeopen function - print command")



if __name__=="__main__":
    unittest.main()
