
from selenium import webdriver

"""
import time
import os
from selenium.webdriver.common.action_chains import ActionChains
import datetime


# Reading of scripts from a notepad/Flat file
fileobj=open("C:/tradedVol/Scrips.txt")
all_scrips=fileobj.readlines()
print (all_scrips)
list_scripts=all_scrips[0].split(",")
print (list_scripts)
list=list_scripts

def OneYeardata(*args):
    path = "C:/tradedVol/chromedriver.exe"
    driver = webdriver.Chrome(path)
    print("This is for downloading data for specific dates\n")
    fromdate = input("Enter Input for From date (format - 01-06-2016):")
    toDate = input("Enter Input for To date (format - 01-06-2017):")
    for arg in args:
        # working on site to extract one year details
        driver.get("https://www.nseindia.com/products/content/equities/equities/eq_security.htm")
        driver.find_element_by_name("symbol").send_keys(arg)
        driver.find_element_by_css_selector("input#rdDateToDate").click()

        #date selection for from date and toddate
        #fromdate=input("Enter Input date (format - 01-06-2016):")
        driver.maximize_window()
        driver.find_element_by_id("toDate").send_keys(toDate)
        driver.find_element_by_id("fromDate").send_keys(fromdate)
        #toDate = input("Enter Input date (format - 01-06-2017):")

        time.sleep(4)

        #click on generate button
        driver.find_element_by_css_selector("img.getdata-button").click()
        time.sleep(4)



        #downloading the data
        f=driver.find_element_by_css_selector("div#historicalData.tabular-data-historic")
        focus_element=f.find_element_by_xpath("//div[@class='historic-bar']/span[2]")
        ActionChains(driver).move_to_element(focus_element).click(focus_element).perform()
        time.sleep(6)

        print (arg +" download success")

OneYeardata(*list)

"""

import glob

all_files=glob.glob1("D:/Users/mkottakk/Downloads","01-06-2016-TO-01-06-*.csv")
print (all_files)

#import panda as pd
import numpy as np
import csv




g=csv.reader(open("D:/Users/mkottakk/Downloads/01-06-2016-TO-01-06-2017ADANIENTALLN.csv","rb"))
print (g)
for row in g:
    print (row)

