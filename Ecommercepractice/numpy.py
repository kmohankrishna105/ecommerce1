"""
#import numpy

d=[1,2,3,4,5]
e=[9,8,7,6,5,3]

i=9.00

print (int(i))
print (float(i),10)
g=(7,8)
print(g)


if len(d)==len(e):
    print ("f")
else:
    print (i)


print (d+e)

#d=input("please:")

if (int(d)>0 and int(d)<100):
    print ("0-100")
else:
    print ("out")


ftxt=open("D:\kmk.txt","r")
x=ftxt.readline()
print (ftxt.readline())

ftxt.seek(10)
print (ftxt.readline())

import xlwt
import xlrd


wb=xlwt.Workbook()
ws=wb.add_sheet("simul")
y=0
for f in x.split():
    f=f.upper()
    ws.write(0,y,f)
    y = y + 1

wb.save("D:/newexcel.xls")

wb.set_active_sheet
#wb.set_colour_RGB(10,10,11,12)


wbr=xlrd.open_workbook("D:/newexcel.xls")
#wbr.get_sheets()
wsr=wbr.sheet_names()
print (wsr)
wss=wbr.sheet_by_index(0)

y=0
for y in range (0,10):
    valu=wss.cell(0,y)
    g=[]

    g.append(valu)
    y=y+1
    print (g)

print (g)


#Exceptions example:

try:

    qw=input("please provide num:")
    if int(qw)%2==0:
        print ("even")
    else:
        print ("odd")
    pass

except:
    print("may not be a number")
    we = input("Would you like to cast the string to number? Y or N")
    try:
        if we.upper()=='Y':
            print (int(qw))
        else:
            print ("Not converting as you wish")
    except ValueError:
        print ("Its a string and cannot be converted")

finally:
    print ("Mission completed")


from selenium import webdriver
from selenium.webdriver.support.expected_conditions import element_to_be_clickable
path = "C:\Python34\chromedriver.exe"
driver=webdriver.Chrome(path)

driver.get("https://www.flipkart.com/mobiles/samsung~brand/pr?sid=tyy,4io&otracker=clp_metro_expandable_1_mobil-categ-fc059_Samsung_mobiles_26069eae-0944-4c1b-a07b-45b626228694_DesktopSite_wp2")

d=driver.find_elements_by_xpath("//*[contains(text(),'Mobile')]")
for mem1 in d:
    print ("Mobile as content are - "+ str(mem1.text))
currency ={'India': "₹"}

for mem in d:
    try:
        h=mem.text
        print (h)
        if h!="":
            try:
                driver.find_element_by_partial_link_text(h).click()
                costitems = driver.find_elements_by_xpath("//*[contains(text(),currency['India'])]")

                for item in costitems:
                    print(item.text)
                    o = driver.find_elements_by_xpath("//*[text(),item]/parent::div/preceding-sibling::div/div]")
                    print(o.text())

                    print (o)
                else:
                    print("No text exists")

            except:
                print (222)


                driver.implicitly_wait(30)
            driver.back()


    except:
        print(h+" Link not found")

#d=driver.find_elements_by_xpath("//*[contains(text(),'Rs')]")

for g in d:
    print (g.text)
"""

from inheritence import parent
from configparser import ConfigParser
import configparser



class child(parent):
    def __init__(self):
        print ("this is a child class")

    def fucn(self):
        print ("this is a overridden function")

obj=parent()
obj1=child()
obj.fucn()


from configparser import ConfigParser

objc=ConfigParser()
objc.read('C:/Users/mkottakk/PycharmProjects/ecommerce/Ecommercepractice/Pages/config.cnf')

first=objc.get('Section1','first')
last=objc.get('Section2','second')
print (first,last)
