
"""
from Ecommercepractice.Classmethods import sequence
import unittest

class terminate(sequence,unittest.TestCase):
    #@classmethod
    def Test_name(self):
        def Test_name2(self):
            print("shi")
        return Test_name2()

if __name__=="__main__":
    unittest.main()

g=terminate

"""
"""
# print the foldder names in mentioned path
import os
from datetime import datetime

print(os.getcwd())
os.chdir("D:\Prudential Content")

print(os.getcwd())
listed=os.listdir()
for name in listed:
    new_listed="D:/Prudential Content/"+ name
    os.chdir(new_listed)
    new_listed1=os.listdir()
    print(new_listed1)
    for name1 in new_listed1:
        try:
            new_listed2 = new_listed+"/" + name1
            os.chdir(new_listed2)
            print(os.listdir())
        except Exception:
            print (name1 + "- Not a folder name")
            try:

                modified_time=os.stat(name1).st_mtime
                d=datetime.fromtimestamp(modified_time)
                print(d)
            except Exception:
                print ("Date attribute does not exists")

"""


class car:
    carcount=0
    height=1.03
    def __init__(self,tyres,steering,glass,cheight):
        self.tyres=tyres
        self.steering=steering
        self.glass=glass
        self.cheight=cheight
        car.carcount=car.carcount+1
        print (car.carcount)

    def Test_height(self):
        self.nheight= int(car.height * self.cheight)
        return self.nheight

    @classmethod
    def set_height(cls,setheight):
        setheight=car.height+0.001
        print ("executed")
        return setheight

    @classmethod
    def splitcar(cls,carstr):
        tyres, steering, glass, cheight= carstr.split("-")
        #return tyres, steering, glass, cheight
        return cls(tyres, steering, glass, cheight)
"""
c1=car("round","left","white",7)
print(c1.__dict__)
print(c1.__sizeof__())
c2=car("flat","left","grey",8)
c3=car("flat","left","grey",9)
c4=car("flat","left","grey",10)
print(c1.glass)
print(c2.glass)

print (c1.height)
print (c1.Test_height())

print (car.carcount)
print("C1 attributes are {} {} {}".format(c1.height,c1.glass,c1.Test_height()))
c2.height=7
print(car.Test_height(c2))
print (c1.__dict__)
print (car.__dict__)


print (c1.height)
print(c2.height)
print(car.height)

print (c2.Test_height())
print (car.Test_height(c1))

print (c3.glass)

# we can call the method by instance
# we can call the method by class and provide the instance as argument
"""

c7=car("j","m","v",100)
print(c7.__dict__)
print(c7.Test_height())

print (c7.height)

#p=c7.set_height(10)
#print (p)

t="flat-left-grey-8"
print(t)
o=car.splitcar(t)
c11=car.splitcar(t)
print (c11.__dict__)
