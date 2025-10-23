# nested if else
n = int(input("enter a number"))

if n > 0:
    print("positive ", end=" , ")
    if n % 2 == 0:
        print("even")
    else:
        print("odd")

elif n < 0:
    print("negative ", end=" , ")
    if n % 2 == 0:
        print("even")
    else:
        print("odd")
else:
    print("zero")
