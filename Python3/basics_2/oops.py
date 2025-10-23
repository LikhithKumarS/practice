class Dog:
    def __init__(self,name):
        self.name=name
    def bark(self):
        print(f"{self.name} wooof")


d=Dog("f")
d.bark()


#handling
try:
    print(1/0)
except ZeroDivisionError:
    print("caught in act")
        
#import
import math
print(math.sqrt(9))