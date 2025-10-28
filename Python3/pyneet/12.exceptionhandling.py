#try catch except

try:
    age_input = input("input")
    age = int(age_input)
    print(f"{age}")
except:
    print("not valid")



try:
    num1 = float(input("num"))
    num2 = float(input("num"))
    res = num1/num2
    print(res)
except ValueError:
    print("error check type")
except ZeroDivisionError:
    print("are you human")


