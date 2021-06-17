
#Set Practice



# 1
#create an empty set and using a fpr loop, add 1 to 10
set1=set()
for i in range (1,11):
    set1.add(i)
print(set1)


# 2
#create another empty set ; for loop add 5 to 20
set2=set()
for i in range (5,21):
    set2.add(i)
print(set2)

#3
#Make a union and intersection of set1 and set2 and analyze the result.
set3=set1.union(set2)
set4=set1.intersection(set2)

print(set1&set2)#intersection
print(set1|set2)#union

#4
# Make a single set population that contains all elements from people and vampires

people = set(["Jay", "Idrish", "Archil"])
vampires = set(["Karan", "Arjun"])
everyone = set()
everyone = people | vampires
print(everyone)

#5
#Write a Python program to remove an item from a set if it is present in the set

if "Jay" in everyone:
    everyone.remove("Jay")
    print(everyone)
else:
    print("Jay not in set")



