# encapsulation
# public default
class Student:
    schoolName = "XSAD"

    def __init__(self, name, age):
        self.name = name
        self.age = age


std = Student("SSss", 65)
print(std.name)
print(std.age)
std.age = 20
print(std.age)


# challenge


class Hero:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
        self._secretmove="Dragon"
        self.__secret_identity = "clark"
        print(f"{self.name} created with HP {hp}")

    def greet(self):
        print(f"hello iam {self.name}")
    def use_special_move(self):
        print(self._secretmove)
    def reveal_secret(self):
        print(f"my secret identity {self.__secret_identity}")


my_hero =Hero("ton",90)
my_hero.greet()
my_hero.use_special_move()
my_hero.__secret_identity()


try:
    
    print(my_hero.__secret_identity)
    
except AttributeError as e:
    print(f"error {e}")


# protected

class Tree:
    def __init__(self,height):
        self.height=height

    def _protected_method(self):
        print("The height is")
        print(self.height)
pine = Tree(23.4)

print(pine.height)
pine._protected_method()
        

