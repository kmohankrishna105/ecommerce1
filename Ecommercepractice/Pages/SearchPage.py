"Methods and elements- Search Page"

class Home():

    def __init__(self,driver):
        self.driver=driver
        
    def Enterstring(self,input):
        self.driver.find_element_by_xpath("//input[@name='search']").send_keys(input)

    def ClickSearch(self):
        self.driver.find_element_by_css_selector("i.fa.fa-search").click()
        self.driver.save_screenshot("D:/Home.png")


"""

class Home():

    def Enterstring(self, driver, input):
        driver.find_element_by_xpath("//input[@name='search']").send_keys(input)

    def ClickSearch(self, driver):
        driver.find_element_by_css_selector("i.fa.fa-search").click()

"""