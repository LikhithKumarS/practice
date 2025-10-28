#sets

set_list=["2","3","2","2","3","2"]
my_set=set(set_list)
print(my_set)

#set operations & |  -

recipe_a={"flour", "sugar", "eggs"}
recipe_b={"sugar","butter","eggs"}

common_ing= recipe_a & recipe_b
allin = recipe_a | recipe_b
uniq= recipe_a - recipe_b

print(f"common {common_ing}, allin {allin} and unique {uniq}")



#set

# applicant_one_skills = ["ruby","on rails","java"]
# applicant_two_skills =["ocaml","bash","q#"]

# setone= set(applicant_one_skills)
# settwo = set(applicant_two_skills)
# print(setone)
# common_st = setone & settwo
# print("commmon",common_st)


# 1 & 2. The initial lists of skills, with a duplicate in the first list.
applicant_one_skills = ["Python", "SQL", "SQL", "Excel", "Communication"]
applicant_two_skills = ["Java", "SQL", "Python", "Problem Solving"]

# 3. Convert each list to a set to get their unique skills.
set_one = set(applicant_one_skills)
set_two = set(applicant_two_skills)

print("Applicant One's unique skills:", set_one)
print("Applicant Two's unique skills:", set_two)

# 4. Find the intersection of the two sets.
common_skills = set_one & set_two

# 5. Print the result.
print("Common skills:", common_skills)