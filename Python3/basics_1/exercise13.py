"""

#print ggg for five times
i=0
print(f"the {i}")
while i<5:
    print("ggg")
    i+=1
    #i=i+1
    print(i+)






"""

"""
# take input and print
n = int(input(("enter the num ")))
i = 0
while i < n:
    print("kkk",i+1)
    i = i + 1

"""
"""
#range
r=range(5)
l=list(r)
print(r,l)
print(type(r))
"""
"""
r = range(20,10,-2)
l=list(r)
print(r,l)



"""
"""
#for loop
#iterables : list tuple string range


l=[1,2,2,3,4]


for x in l:
    print(x)
    print("diff",l[x])


for x in range(21):
    if x % 6 == 0:
        print("the number divided by ",x)


"""

"""
n =int(input("enter n"))
m =int(input("enter m"))


i=1

while i<=m:
    print(i*n)
    i=i+1
 
"""

# break statement
"""
n =int(input("enter n"))
for x in range(2,n+1):
    if n % x == 0:
        print(x)
        break
        
"""
"""            
i=1
while i<=5:
    if i ==3:
        break
    print(i, " ...")
    i+=1
print(i)

"""
"""
r = range(17,45)
l =list(r)
print(l)
for x in l:
    if x % 5 == 0:
        print("fiverr")
        continue
    print(x)

    
"""
"""
i=-10
while i<=5:
    if i == 3:
        i +=1
        continue
    print(i, i*i)
    i +=1

"""


"""
for i in range(1, 11):
    for j in range(i, i * 10 + 1, i):
        print(j, end="  ")
    print(j * "₹")
"""
n = int(input("Enter n"))
for i in range(n):
    for j in range(i+1):
        print("*", end="")
    print("...")