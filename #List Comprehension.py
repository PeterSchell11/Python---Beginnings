#List Comprehension

list1=[1,2,3,4]
list2=[item**2 for item in list1]
print(list2)

str_list=['John','Ken','April'] 
len_list=[]
for s in str_list: 
	len_list.append(len(s))
print(len_list)


len_list=[len(s) for s in str_list]
print(len_list)


