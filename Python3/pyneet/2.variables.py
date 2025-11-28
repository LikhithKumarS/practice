"""
variable declaration - storing value and assigning  to a named  reference
variable naming - Naming conventions
Reassigning variables
variable types


"""

favorite_color = "blue"
print("my fav color is ", favorite_color)


player_level = 1
print("initial level", player_level)
player_level = 2
print("initial level", player_level)


# multiple assignments
x, y, z = 0, 1, 3
print(x, y, z)

a = b = c = 0
print(a, b, c)


knight_health = archer_health = wizard_health = 0

print(
    "The game starts",
    "knight",
    knight_health,
    "archer",
    archer_health,
    "wizard",
    wizard_health,
)


# variable types
# string str
# number int float

player_name = "gandalf"
player_age = 11
player_score = 99.98
print("Name:", player_name, type(player_name))
print("Age:", player_age, type(player_age))
print("Score:", player_score, type(player_score))


temp = "gandalf"
print(temp, type(temp))
temp = 11
print(temp, type(temp))
temp = 222.442
print(temp, type(temp))


# combining sting and integers

score = 500
print("The score is ", score)
print("Your final " + str(score) + " points only")

# type casting
num1 = 1
num2 = "5"
"""
result = num1+num2
result = num1+num2
             ~~~~^~~~~
TypeError: unsupported operand type(s) for +: 'int' and 'str'
"""
result = num1 + int(num2)
print(result, "sum of 2 numbers")
print("-----------------------------------------------------------------------------")

# the concept of Nothing --> None
# 1. Initialize the prize to None because it's not yet known.
grand_prize = None

# 2. Print the initial status.
print("The grand prize is currently undecided.")

# Some time passes...

# 3. The prize is decided, so we reassign the variable.
grand_prize = "a trip to Hawaii"

# 4. Announce the prize.
print("The grand prize has been announced! It is:", grand_prize)
