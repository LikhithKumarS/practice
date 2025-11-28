def greet(name):
    return "hello "+name

message = greet("Allie")
print(message)


#array/list

number = [1,2,2,123]
number.append(5)
print(number)


s="hhheelllooo"
print(s.upper())
print(len(s))

#pointers
a=[1,3]
b=a
b.append(5)
print(b)
print(a)