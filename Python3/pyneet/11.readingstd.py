#input()
'''
username= input("\twhats your name\n")

print(f"{username}")



user_age = input("whats year of birth")
current_year= 2025
u=current_year-int(user_age)
age = int(u)+1
print(age)
'''

#.split()

input1 =(input("enter w & h"))
print(input1,type(input1))
parts=input1.split()
print(parts)

w=int(parts[0])
h= int(parts[1])
area=w*h
print(f"w {w},h {h} and area as {area}, parts {parts}")


input2 = input("enter number one after another")
print(input2)
partsz= input2.split()
a=float(partsz[0])
b=float(partsz[1])
print(a,b)

flo =  a+b
print(flo)