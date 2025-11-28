"""n = int(input("enter a number"))
if n % 2 == 0:
    print("you")
else:

    print("opp")"""

import sys

'''
a = int(input("enter First number \n"))
b = int(input("enter Second number \n"))
c = int(input("enter Third number \t"))
'''
''' 
if a >= b and a >= c:
    print("a is largest")
if b >= a and b>=c:
    print("b is largest")
else:
    print("c is largest")

'''
'''
if a is greater than or equal to b AND a is greater than or equal to c
if b is greater than or equal to a AND b is greater than or equal to c
if c is greater than or equal to a AND c is greater than or equal to b



'''
'''
if a>=b:   #check if a or b if b go to else b>=c
    if a>=c: #check if a or c print c as iterated with a, b and found c is larger
        print(a) 
    else:
        print(c)
else:
    if b>=c:
        print(b)
    else:
        print(c)
        
        
        
print(max(a,b,c))

'''


'''  
y= int(input("y"))
if(y%4==0) and (y%100!=0):
    print("yes")
elif (y%4==0):
    print("yes")
else: 
    print("nah")
    
    
    '''
    
    
    #calcy
print(""" 
      Please select operation:
      1:ADD
      2:SUBtract
      3:MULTIPLY
      
      """)

choice=int(input("Select 1,2 OR 3 \n"))

if choice not in (1,2,3):
    print("Dude cant ya type number")
    sys.exit()


a = int(input("enter First number \n"))
b = int(input("enter Second number \n"))

if choice ==1:
    res =a+b
elif choice ==2:
    res=a-b
else:
    res =a*b
print("Result is",res)

