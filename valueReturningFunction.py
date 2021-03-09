#writing your own value returning functions

#a value returning function

def greeting():
    print("hello, world")
greeting()

def returnGreeting():
    return "Hello World"
returnGreeting()

def number():
    print(5)
def number1():
    return 5
number()
number1()
print(number1())#return vs print


def sum(a,b):
    result = a + b
    return result
print(sum(2,2))

def main1():
    firstNum = int(input("enter interger: "))
    secondNum = int(input("enter anothe interger: "))

    total = sum(firstNum,secondNum)
    #print (total)
    print(f'The sum of {firstNum} and {secondNum} is {total}')
main1()

def main2():
    firstNum = int(input("enter interger: "))
    secondNum = int(input("enter anothe interger: "))

    total = product(firstNum,secondNum)
    print(f'The product of {firstNum} and {secondNum} is {total}')
    #print (total)

def product(a,b):
    return (a*b)#dont need to asign to a variable
    
    
main1()