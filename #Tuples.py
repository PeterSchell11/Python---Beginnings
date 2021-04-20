#Tuples
	#sequence, like a list, but contents cannot be changed

my_tuple=(1,2,3,4,5)
print(my_tuple)

names=('John','Ken','Kelly','Sam')
for n in names: 
	print(n)

#Converting Between Lists and Tuples
numTuple=(1,2,3)
numList=list(numTuple)
print(numList)

str_list=['one','two','three']
str_tuple=tuple(str_list)
print(str_tuple)