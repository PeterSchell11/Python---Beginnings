#Using if Clauses with List Comprehensions

#Want to make a second list which only contains integers less than 10
list1=[1,4,2,5,10,12,45,32,8,15] 
list2=[]
for n in list1: 
	if n<10:	
		list2.append(n)
print(list2)

list3=[item for item in list1 if item<10]
print(list3)
list3.sort()

last_names=['Jackson','Smith','Harry', 'Jones', 'Tan'] 
short_names=[name for name in last_names if len(name)<6]
print(short_names)