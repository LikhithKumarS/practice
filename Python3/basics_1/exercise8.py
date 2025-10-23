'''

#AP a,d,(n-1)
a=int(input("Enter a : "))
d=int(input("Enter d : "))
n=int(input("Enter n : "))


#core logic
result= a+(n-1)*d
print(result)

''' 


'''
#gp
#a*(r**(n-1))
a=int(input("Enter a : "))
r=int(input("Enter r : "))
n=int(input("Enter n : "))

resultgp= a*(r**(n-1))
print(resultgp)

'''
'''
#sum of natural numbers
#n*(n+1)/2

n=int(input("enter n:"))
sum = n*(n+1)/2
#mult precedence
print(int(sum))

'''
'''
#last digit of the given number

x=(int(input("enter x")))
print(x)
ld= abs(x)%10
print(ld)


'''

#DAY BEFORE N DAYS
# (d-n)%7

d=int(input("Enter d : "))
n=int(input("Enter n : "))

print((d-n)%7)


