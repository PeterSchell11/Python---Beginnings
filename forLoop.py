#The for Loop

    #format : forVariable  in [value1, value2, etc]
    #automatically gives it a type --> remembers last outputs type

for number in[1,2,3,4,5]:
    print(number)
print(type(number))

for name in['Mark', 'Peter','Jackie' ]:
    print(name)
print(type(name)
print("\n")

#range function with for loop

for x in range(5):
  print("x")

for x in range(10):    #doesnt work in idle for some reason
  if x%2!=0:
    print(x)
for num in range(2,5):
  print(num)

for num in range(1,10,2): # Prints every two numbers
   print(num)

for num in range (0,21,2):
    print(num)

    using target variable in for loop

#('\t') tab

print('Number \t Square\n')
print('--------------------')
for num in range (1,10):
  square = num**2
  print (f'{num}\t\t{square}')

print('Fahrenheit \t Celcius\n')
print('--------------------')
for f in range (50,101,5):
  celcius = (f-32)*1.8
  print (f'{f}\t\t\t{celcius}')