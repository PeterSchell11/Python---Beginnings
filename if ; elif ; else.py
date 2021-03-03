

#if ; elif ; else

x = int (input('Pick a number between 1 and 7: \n'))

if x == 1:
    print('Monday')
elif x == 2:
    print('Tuesday')
elif x == 3:
    print('Wednsday')
elif x == 4:
    print('Thursday')
elif x == 5:
    print('Friday')
elif x == 6:
    print('Saturday')
elif x ==7:
    print('Sunday')
else:
    print ('There is an error')

#example 2 with a persons age
x= float (input(' Enter a Person\'s age: \n'))

if x>0 and x<=1:
    print('This person is an infant')
elif  x < 13:
    print('This person is an child')
elif x >= 13 and x < 20:
    print('This person is a teen')
elif x >= 20 and x<120 :
    print('This person is an adult')
elif x >= 120:
    print('You are either dead or old')
else:
    print('Fetus')



#Example 3 with test score
x = int (input('Enter Score \n'))

if x >= 0 and x < 70:
    print('Your grade is a F')
    
elif x >=70 and x < 80:    
    print('Your grade is a C ')
    
elif x >= 80 and x < 90:    
    print('Your grade is a B ')
    
elif x >= 90 and x <= 100:
    print('Your grade is a A ')

else: 
    print('error')

