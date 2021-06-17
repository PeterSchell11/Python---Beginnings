#Calculator

def add(x,y):
    return x+y

def subtract(x,y):
    return x-y
    
def multiply(x,y):
    return x*y
    

def divide(x,y):   
    return x/y

def calculator():
  print('Menu:\n 1 - addition \n 2 - subtraction \
  \n 3 - multiplication \n 4 - division \n 0 - quit\n')

  w=0
  while w==0:
    choice = input("Enter choice(1/2/3/4/0): ")

    if choice in ('1','2','3','4'):
      
      num1 = float(input("Enter first number : "))
      num2 = float(input("Enter second number : "))
        
      if choice == '1':
        print (f'{num1} + {num2} = {add(num1,num2)}\n')
      elif choice == '2':
        print (f'{num1} - {num2} = {subtract(num1,num2)}\n')
      elif choice == '3':
        print (f'{num1} * {num2} = {multiply(num1,num2)}\n')
      elif choice == '4':
        print (f'{num1} / {num2} = {divide(num1,num2)}\n')
      
    elif choice == '0':
      w=1

    else :
      print("Invalid Input!\n")


calculator()