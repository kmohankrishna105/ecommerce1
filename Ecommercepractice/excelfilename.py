
"""
# export tab names form excel sheet
import xlrd
path=input("Enter sheet path:")
name=input("Enter file name:")
wb=xlrd.open_workbook(str(path+'/'+name))
ws=wb.sheet_names()
for sheet in ws:
    print (sheet)
"""
# create an excel sheet with required sheet names
import xlwt
import pdb

wb1=xlwt.Workbook("Hai.xls")
snames=input("sheet name :")
individual=snames.split(",")
#print((pdb).line_prefix)

for s in individual:
    ws1=wb1.add_sheet(s)

    print(s+" - sheet created")
    #pdb.set_trace()

wb1.save("D:/Hai.xls")

f=wb1.sheet_
print (f)
# publish values in report (matrix format)
"""
import xlwt
i=0
j=0
wb2=xlwt.Workbook("jumble.xls")
ws=wb2.add_sheet("numbers")
for j in range(0,26):
    i=0
    ws.write(i,j,j)
    i=1
    for i in range(1,26):
        ws.write(i, j, i)
        i=i+1
    j=j+1
wb2.save("D:/jumble.xls")
"""
#
