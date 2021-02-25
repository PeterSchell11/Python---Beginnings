

import random
print(random.randrange(1,100))

#Specifying an Item Seperator

print ('one','two','three')
print('One','Two','Three', sep='')
print('One','Two','Three', sep='*')

#Reading input from the keyboard

FirstName = input('Enter First name: ')
LastName= input ('Enter Last Name:')
print('Hello ',FirstName ,LastName)

#Reading Number with print function

number=input('What is the number?')
print(type(number))

stringvalue=input("how many hours did you work")
hours=int(stringvalue)
print(hours, type(hours))

#f-strings

print(f'Hello world')
name='john'
print(f'hello {name}')

temp = 45
print(f'it is currently {temp} degrees')

print(f'the value is {10+2}.')
val=10
print(f'the value is {val+2}.')

debt=5000.0
payment=debt/12.0
print(f'Your monthly payment is {payment:.2f}')
        #:.2f is decimal points for output
a=2
b=3
print(f'{a/b:.1f}')

number = 123456789.1234
print(f'{number:,}')# separates commas output - 123,456,789.1234
print(f'{number:,.2f}')#includes commas and only 2 decimals


#formatting a foating- point number as a percentage

discount=0.5
print(f'{discount:%}')
print(f'{discount:.0%}')

#formatting intergers

number=123456.1234
print(f'{number:,}')

number=123456
print(f'{number:,d}')#d and f are for int







