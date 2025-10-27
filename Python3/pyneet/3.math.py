'''
| Arithmetic Operators | Performing basic mathematical calculations (+, -, *, /).   |
| -------------------- | ---------------------------------------------------------- |

'''


'''

- **Problem:** You are at a grocery store and want to calculate the total cost of three items.
    
    1. Create variables for the price of an apple (`0.50`), a loaf of bread (`2.00`), and a carton of milk (`1.50`).
        
    2. Create a `total_cost` variable that adds the prices of all three items together.
        
    3. Print the `total_cost`.

'''


_apple =0.50
_loaf_of_bread = 2.00
_a_carton_of_milk = 1.5

total_cost= _apple+_loaf_of_bread+_a_carton_of_milk
print(total_cost)


#exponential 
num1=2
exp=num1**2
print(exp)

##floor division


'''
**Problem:** You have 20 cookies and want to share them equally among 3 friends.
    
    1. Use floor division (`//`) to calculate how many cookies each friend gets.
        
    2. Use the modulo operator (`%`) to calculate how many cookies will be left over for you.
        
    3. Print both results with clear explanations.
'''

_cookies = 20
_friends = 3
distribution = _cookies//_friends
print(distribution,"number of cookies each friend gets")

remainder = _cookies%_friends
print("Left out cookies after distribution",remainder)

#score = score + 10
score = 0
print(score)

score += 10
print(score)


score =score+20
print(score)

score -=6.7
print(score)
    # 1. Start the score at 0.
score = 0
print("Starting Score:", score)
    
    # 2. Add points for the treasure.
score += 50
print("Found treasure! Current Score:", score)
    
    # 3. Subtract points for the trap.
score -= 15
print("Hit a trap! Current Score:", score)
    
    # 4. Print the final result.
print("Final Score:", score)



golden_key =False
magic_scroll =True
opensesme = golden_key or magic_scroll

if opensesme:
    print("highness you are back")
else:
    print("banish the witch")

sudo_opensesme =golden_key and magic_scroll 
if sudo_opensesme:
    print("highness you are back")
else:
    print("banish the witch")

print(opensesme)
print(sudo_opensesme)


#Not : not operator
is_guard_looking = False
is_safe_to_enter = not is_guard_looking
print("Is it safe to enter?", is_safe_to_enter) # This will print True