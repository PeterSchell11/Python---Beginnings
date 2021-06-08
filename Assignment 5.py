#Peter Schellhorn
#Loop printing 0-100 that are divisable by 7

for x in range(101):
	if x%7==0:
		print (x)

#Loop printing 0-100 that are divisable by 5 but not 3 

for x in range (0,100):
	if (x%5==0) and (x%3!=0):
		print(x)

#while loop to find sum of first 50 

y=0
z=0
while z <0 50:
	y=y+z
	z+=1
print (y)	

#while loop for factorial of 15
i=0
a=1
while i<a:
	for i in range (1,16):
		a = a*i 
		i +=1 
print (a)

#or
#n=15
#f=1
#x=1
#while x<=n:
#	f=f*x
#	x=x+1
#print ("f")
	