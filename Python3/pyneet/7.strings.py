#indexing
#len

user_name="hello, the !!@!"
user_len = len(user_name)
print(user_len,user_name)
print("Is the username long enough?", user_len >= 5)

#Extracting Specific Information
name = "python"
first_letter =name[0]
last_letter = name[-1]
print(first_letter,last_letter)


#string looping

code= "wordle"
for i in range(len(code)):
    print(i,code[i])

#foreach
name = "beatrice"
vowel_counter =0
for char in name:
    if char.lower() in "aeiou":
        print(char)
        vowel_counter +=1
    print("name has", char, vowel_counter )



#joining Strings
#concat 

 # 1. The two pieces of the name.
first_name = "Ada"
last_name = "Lovelace"
    
    # 2. Concatenate the strings.
full_name = first_name + " " + last_name
    
    # 3. Print the result.
print("The full name is:", full_name)



sentence = "The quick brown fox jumps over the lazy dog"
for i in range(len(sentence)):
    print(sentence[i],end="")
print(i)
print(sentence[40:43])
print(sentence[:16])
print(sentence[30:])



#palindrome

word = "racecar"
reverse_word = word[::-1]
print(reverse_word)
is_palindrome = word == reverse_word
print(is_palindrome)

'''    
#immutable strings
greet ="pello"
greet[0]="H"

print(greet)



Traceback (most recent call last):
  File "/Users/vishnuprasad/Documents/Practice/practice/Python3/pyneet/7.strings.py", line 69, in <module>
    greet[0]="H"
    ~~~~~^^^
TypeError: 'str' object does not support item assignment
'''

greet ="pello"
corrected_string = "H" +greet[1:]
print(corrected_string)

#string formatting

#f-string

'''
name ="alei"
age=79
city='new york'
print("Your name is "+name," "+" you are "+age+" years old, and you live in New York.")


Traceback (most recent call last):
  File "/Users/vishnuprasad/Documents/Practice/practice/Python3/pyneet/7.strings.py", line 92, in <module>
    print("Your name is "+name," "+" you are "+age+" years old, and you live in New York.")
                               ~~~~~~~~~~~~~~~^~~~
TypeError: can only concatenate str (not "int") to str


'''
#use f string
name ="alei"
age=79
city='new york'

summary = f" your name is {name}, you are {age} and from {city}"
print(summary)