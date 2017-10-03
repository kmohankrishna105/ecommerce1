import math
from pptx import Presentation
from pptx import slide
from pptx.slide import _BaseSlide
from pyechonest import config


class dog():
    def __init__(self, breed,name):
        self.breed=breed
        self.name=name
        #print("Is the breed " + breed)

    def __str__(self):
        return self.name

    def __len__(self):
        return 1000001

    def __invert__(self):
        return "invert"

    def __del__(self):
        print ("Book deleted for ever")



p=dog("hik","rik")

print(p)

print(len(p))

print(p)

del p

print(type(1))

print(type({"f":1}))

print(type("ft"))

print(type([3,4,5]))

print(type((3,4,5)))

def fun():
    pass

print(type(fun))

class cla:
    pass

#print(type(cla))

c=cla()

print(type(c))
print(c)

class Car:
    #class object attributes
    obj_type="transport"

    def __init__(self,name,model,cond=True):
        self.name=name
        self.model=model
        self.cond=cond
        print ("Car name - {}, model-{}".format(self.name,self.model))

    def __str__(self):
        return "Built in str function called"


d=Car("Pinto",2015)
print(d)

print(d.name)
print(d.cond)
e=Car("Figo",2016,False)
print(e.cond)


from backport_collections import defaultdict
from collections