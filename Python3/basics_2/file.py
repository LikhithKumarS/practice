with open("sample.txt", "w") as f:
    f.write("asdf")


# read
with open("sample.txt", "r") as r:
    f = r.read()
    print(f)


# recursion
def fact(n):
    return 1 if n == 0 else n * fact(n - 1)


print(fact(5))


# lamda

square = lambda x: x ** 2
print(square(4))
