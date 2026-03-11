import math


def getFirstDigit(x):
    while x >= 10:
        x = x // 10
        print(x)
    return x

def getFirstDigitUsingLog(x):
    d=int(math.log10(x))
    res=x//(10**d)
    print(d,res)
    return res


x = int(input("Enter x:"))
print(getFirstDigitUsingLog(x))
