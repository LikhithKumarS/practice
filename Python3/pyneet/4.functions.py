#makecoffe

def make_coffe():
    print("boil water")
    print("Put coffee grounds in a filter.")
    print("Pour water over the grounds.")
    print("Add milk and sugar.")

make_coffe()

def send_greeting():
    print("greetings")

send_greeting()

def send_greeting(name):
    print("hello",name)


send_greeting("alllie")

#twoparams
def pet_intro(animal,name):
    print("its ",animal)
    print("Hello",name)

pet_intro("dog","fido")
pet_intro("dog","")
pet_intro(animal=0,name=1)


#return get the answer back

def add(num1,num2):
    return num1+num2
sum_res= add(34,5)
print("The sum",sum_res)


def i_add(num1:int,num2:float)->float:
   return num1+num2 
sum_result=add(4,4)
print("The sum",sum_result)

'''
#scope
def create_a_message():
    message="secret"
    print(message)

create_a_message()

print(message)

'''


location = 'earth'
def change_location():
    print("inside function")

print(location)
change_location()

#default
def gret(name,message="hello"):
    print("oh",name,message)

gret("josh",'kilo')
gret("allie")