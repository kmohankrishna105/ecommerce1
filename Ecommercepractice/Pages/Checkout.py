class Checkout:

    def __init__(self,driver):
        self.driver=driver

    def Newmember(self):
        self.driver.find_element_by_css_selector("input[value='guest']").click()
        self.driver.find_element_by_xpath("//input[@value='Continue']").click()
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_id("input-payment-firstname").send_keys("FirstName")
        self.driver.find_element_by_id("input-payment-lastname").send_keys("LastName")
        self.driver.find_element_by_id("input-payment-email").send_keys("Email")
        self.driver.save_screenshot("D:/Checkout.png")