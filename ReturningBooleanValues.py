#returning boolean values

def isEven(num):
    if (num%2==0):
        status=True
    else:
        status=False
    return status

numb=int(input("Enter number: "))
if isEven(numb):
    print(f'The number {numb} is even')
else:
    print (f'The number {numb} is odd')
