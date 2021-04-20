#Two Dimensional Lists

students=[['Joe', 'Kim'],['Sam','Sue'],['Kelly','Chris']] 
print(students)
print(students[0])
print(students[1])
print(students[2])

def main():
#Create a two dimensional list
	values=[[1,2,3], 
			[10,20,30],
			[100,200,300]] 
	for row in values:
		for element in row: 
			print(element)
main()


import random
rows=3 cols=4
def main1(): 
	values=[[0,0,0,0],
       [0,0,0,0],
       [0,0,0,0]]

for r in range(rows):
	for c in range(cols):
		values[r][c]=random.randint(1, 100) 
print (values)

main1()

import random
rows=2 cols=2

values=[[0,0],
       [0,0]]

for r in range(rows):
	for c in range(cols):
		values[r][c]=random.randint(1, 10) 
print (values)




