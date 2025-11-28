#while loops
user_input=""
while user_input!= "exit":
    print("hello")
    user_input=input("\twhat you would like to do\n")
print("gbu")


#repeat task 

count =5
while count>0:
    print(count)
    count -=1
print("blast")


#for loop
for chapter in range(1,6):
    print(chapter,"chapter")

#for loops skipping
# even
for n in range(2,11,2):
    print(n,"even")    

#-1 steps for loop

for n in range(5,0,-1):
    print(n,"counting...")
print("blast off")


#nested loops
#star
for row in range(3):
    for col in range(3):
        print("*", end="")
    print(" ~ ")


#while loops multiplier sequence

mul=1
while mul <=5:
    result =3*mul
    print(result)
    mul +=1
print("done")

for i in range(4):
    print("are we there yet",i)
print("reached")


#break & continue
for i in range(1,10):
    
    if i ==5:
        print("skipping 5")
        continue
    if i ==9:
        print(" killed")
        break
    print("*",i)
print("loop-ended")


