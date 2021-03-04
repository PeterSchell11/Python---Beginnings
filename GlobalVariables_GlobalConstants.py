#Global Variables and Global Constants

myValue = 10 #global Number
def showValue():
    print(myValue)
showValue()

##########################

number= 0#global number
def main():
    global number #do this so you can change the global number from inside function
    number=int(input('Enter a Number'))
    showNumber()
    print (number)
    
def showNumber():
    print(f'THe number you entered is {number}')

main()

print('########################')
##########################


