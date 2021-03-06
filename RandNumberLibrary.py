
#Random Number Library

import random

x = int(input('How many random numbers: '))
y = 1
def randomNum():
    for randomNum in range(x):
        print( random.randrange(1,100))
                                #randrange does not include 100

        
randomNum()

def randomNum2():
    for i in range(6):
        print(random.randint(1,100))
                    #includes the 100
randomNum2()

