#key value pairs
'''
1. unordered
2.mutable
'''


user_profile={
    "name":"k",
    "age":6
}
print(user_profile)
print(user_profile["name"])


for item,details in user_profile.items():
    print(f"item:{item}, details:{details}")



#dictionary
inventory={}

inventory["apples"]=10
inventory["ban"]=15
inventory["orange"]=0.342
inventory["apples"]=2
print(inventory)
inventory["ban"] -= 4
inventory["orange"] -=1
del inventory["apples"]

exp = inventory.values()
tot = sum(exp)
print(tot)
print(inventory)




