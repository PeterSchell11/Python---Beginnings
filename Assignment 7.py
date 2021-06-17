
#Peter Schellhorn
#Hw7

def add(x,y):
    z=x+y
    print(f'{x} added to {y} is equal to {z}\n')
    return z

def subtract(x,y):
    z=x-y
    print(f'{x} subtracted by {y} is equal to {z}\n')
    return z
    
def multiply(x,y):
    z=x*y
    print(f'{x} multiplied by {y} is equal to {z}\n')
    return z
    

def divide(x,y):
    z=x/y
    print(f'{x} divided by {y} is equal to {z}\n')
    return z

def menu():
    
    menu = 1
    while(menu!=0):
    
        num1=float(input("Enter first number: "))
        num2=float(input('Enter second number: '))
    
        print('Menu:\n 1 - addition \n 2 - subtraction \
\n 3 - multiplication \n 4 - division \n 0 - quit')
        inpt = int(input('\nEnter numer corresponding to what you want to do with these numbers?: ')) 

        if(inpt==1):
            add(num1,num2)
        if (inpt==2):
            subtract(num1,num2)
        if (inpt==3):
            multiply(num1,num2)
        if (inpt==4):
            divide(num1,num2)
        if (inpt==0):
            menu = 0

menu()
       
            
    
    

