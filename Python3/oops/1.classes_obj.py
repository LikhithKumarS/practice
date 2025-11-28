class MyClass:
    """A simple class"""
    i=12345

    def f(self):
        return "hello friend"
    
    ''' 
    i is an attribute
    f is a method

    pep 
    classname should be pascal case || PascalCase

    '''

class Pet:
    pass



#object 
''' 
object is also called as instance of the class

obj Class instantiation
# Assuming MyClass is defined
x = MyClass()

obj variable naming pep snake case
TO instantiate call class followed by parentheses MyClass()

'''
# class Book:
#     pass
# book_1 = Book()
# book_2 = Book()
# print(book_1)
# print(id(book_2))




#object Attributes
'''
Data stored inside a class or object is called an attribute.   


class Dog:
    kind = 'canine'         # class variable shared by all instances

    def __init__(self, name):
       ...[source](https://discuss.codecademy.com/t/if-an-instance-variable-is-not-set-in-init-can-it-be-referenced-by-a-class-method/359146)

       class ClassName:
    attribute_name = "some_value"
    pass
'''


class Book:
    genre="non fiction"
    pass

    def start_reading(self):
        print(f"you must open the book to start reading {self.genre}")
        print(id(self)) #printing id of book and self to confirm their memory


book1=Book()
print(book1.genre)
book1.start_reading()

print(id(book1))
'''nside the class Book: block, we add the line genre = "non-fiction". Because this is defined directly in the class (and not inside a function), it becomes a class attribute.'''


#object methods
x=MyClass()
print(x.f())

#scroll up for the MyClass

class ClassName:
    
    # A method definition
    def method_name(self, parameter1, parameter2):
        # Method body
        print(f"Got {parameter1} {self} {parameter2}")

# To call the method, you use dot notation on an object
my_object = ClassName()
my_object.method_name("value1", "value2")



class Complex():
    def __init__(self,realpart,imagpart):
        self.r=realpart
        self.i=imagpart
        pass

x=Complex(2,-4)    
print(x.r,x.i)


class Movie:
    genre="horror"
    def __init__(self,title,author):
        self.title = title
        self.author = author
        print(f"{self.title }{self.author }")
        pass
    def start_reading(self):
        print(f"You start reading '{self.title}' by {self.author}.")
book_2 = Movie("Dune", "Frank Herbert")
book_2.start_reading()


#docstrings across ''' docstrings '''

class SuperHero:
    def __init__(self,name,secret_identity):
        self.name=name
        self.secret_identity=secret_identity
        self.powers = []
    def add_power(self,new_power):
        self.powers.append(new_power)
        print(new_power)
    def reveal_identity(self):
        print(f"My secret identity is... {self.secret_identity}!")


spidey=SuperHero("Spiderman","peter-parker")
print(f"the hero{spidey.name}")
print(f"the secret identity {spidey.secret_identity}")
spidey.add_power("wall_crawl")
print(f"{spidey.name} has these powers: {spidey.powers}")
spidey.reveal_identity()


