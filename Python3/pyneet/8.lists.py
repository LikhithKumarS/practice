#list=[,]

my_todo=["wakeup","code"]
print(my_todo,"my todos")
has_code= "code" in my_todo
print(has_code)
#in keyword

grocery_list=["bread","eggs","cheese"]
has_milk="milk" in grocery_list
presence=f"{grocery_list} and {has_milk}"
print(presence)

#looping

players=["kkb","ccb","csk"]
print(players[0])
for i in range(len(players)):
    print("welcome aboard",players[i])
    


#list are mutable
my_todo=["wakeup","code"]
print("current list",my_todo)
my_todo.append("run")
print("updated_list",my_todo)

for i in range(len(my_todo)):
    my_todo.append(i)

print("updated_list",my_todo)
# list takes one arg
'''
Traceback (most recent call last):
  File "/Users/vishnuprasad/Documents/Practice/practice/Python3/pyneet/8.lists.py", line 30, in <module>
    my_todo.append(i,"")
    ~~~~~~~~~~~~~~^^^^^^
TypeError: list.append() takes exactly one argument (2 given)


'''


#list_pop()

#completing a task
todos=["eat"]
todos.append("sleep")
todos.append("repeat")
todos.append("repeat")
print(f"{todos}")
todos.pop()
print(f"{todos} done")
todos.pop()
print(f"{todos} done")
todos.pop()
print(f"{todos} done")
todos.pop()
print(f"{todos} done")

#list find
#.index()

runners = ["cha","ka","csk","rcb"]
runners.index("cha")
print(runners)
rcb_index=runners.index("rcb")
print(rcb_index)
rank_rcb=rcb_index+1
print("rank of rcb",rank_rcb)


#list slicing
print(runners[:3])
winner = runners[0]
print(winner,"winner ")




#tuple
#immutable list

#my_tuple=("1",5)

co_ord=(1,4,5)
print(co_ord)
print(type(co_ord))
#co_ord[2]=3
print(co_ord)

'''<class 'tuple'>
Traceback (most recent call last):
  File "/Users/vishnuprasad/Documents/Practice/practice/Python3/pyneet/8.lists.py", line 90, in <module>
    co_ord[2]=3
    ~~~~~~^^^
TypeError: 'tuple' object does not support item assignment'''