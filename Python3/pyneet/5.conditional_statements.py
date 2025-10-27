# comparison


"""

- `==` : Is equal to?

- `!=` : Is not equal to?

- `>` : Is greater than?

- `<` : Is less than?

- `>=` : Is greater than or equal to?

- `<=` : Is less than or equal to?


"""

my_age = 52
is_old_en = my_age >= 13
print(is_old_en)


# ifstatement
is_raining = True

if is_raining:
    print("rain coat")
print("good day")


# if statement scope

# if
"""
    # Broken Code
player_score = 85
    
if player_score > 90:
    bonus_points = 10
    print("Your bonus points:", bonus_points)

      
      # bonus_points is only created if the score is high enough
      
"""

# fix

player_score = 85
bonus_point = 0
if player_score > 90:
    print(bonus_point)

print("Your bonus points:", bonus_point)


# if else statement
is_daytime = False
if is_daytime:
    print("turn off light")
else:
    print("Turn on lights")

# else -if statements
light_color = "red"
if light_color == "green":
    print("go")
elif light_color == "yellow":
    print("get ready")
else:
    print(" stop")

#and or not

is_weekday =False
is_vacation=False

if is_weekday and not is_vacation:
    print("work")
else:
    print("sleep")

#truthiness 

'''

- **Falsy:** Values that are considered `False`. These include 
`0`,
 `""` (an empty string),
   `` (an empty list),
     `None`,
       and 
       `False`
         itself.
    
- **Truthy:** Pretty much everything else. Any non-empty string, any non-zero number, and any non-empty list is considered `True`.
    
'''
user_name = "dd"
if user_name:
    print("hello",user_name)
else:
    print("enter name")

