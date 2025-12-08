

# n = int(input("enter n \n"))
# for i in range(n):
#     for j in range(n-i-1):
#         print(" ",end=" ")
#     for k in range(2*i+1):
#         print("*",end=" ")
#     print()




#count number of digits in 9253
# x = float(input("enter n \n"))
# res=0
# while x>0:
#     x=x//10
#     print(x,res)
#     res +=1

# print("the digits",res)




n = int(input("enter n \n"))
res=1
print(res,end=" ")
for i in range(2,n+1):
    res *= i
    print(i,res,end=" ")
print(" factorial is ",res)