
#Assignment 4 - Peter Schellhorn

#Problem 1



length1 = int(input('Length of first rectangle'))
width1 = int(input('Width of first rectangle'))

length2 = int(input('Length of second rectangle'))
width2 = int(input('width of second rectangle'))

area1 = length1 * width1
area2 = length2 * width2

if (area1 > area2) :
    print('The area of the first rectangle is greater than the area the second rectangle')

if (area1 < area2) :
    print('The area of the first rectangle is lesser than the area the second rectangle')

if (area1 == area2) :
    print('The area of the first rectangle is equal to the area  the second rectangle')


#problem 2

print ('Lets determine if a triangle is a right triangle')

angle1 = int(input('Enter the first angle of your triangle'))
angle2 = int(input('Enter the second angle of your triangle'))

 #always right triangle

if (angle1 + angle2) == 90 :
    print('Your Triangle is a right triangle')
else :
    print('Your Triangle is a not right triangle')

#Problem 3

base_gallon = 3000
waterUsed = int(input('How much water in gallons did you use this month'))
pricePerGallon= int (input ('what is the price per gallon'))
extra = 2 + pricePerGallon
difference = waterUsed - base_gallon

if (waterUsed == base_gallon):
    print('Bill this month is $')  
    print(base_gallon * pricePerGallon)
          #how do you put both on the same line/print
if (waterUsed > base_gallon):
    print('Bill this month is $')
    print((base_gallon * pricePerGallon)+(difference * extra))
   
