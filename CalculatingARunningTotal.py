
# Calculating a Running Total
MAX = 4

total = 0.0

print ('this program calculates sum of ',MAX, ' numbers')
for counter in range(MAX):
    number = int(input('enter number: '))
    total = total + number
                 
print (total)


days = 5
total = 0.0
print ('How many bugs have you collected on each day')
for counter in range(days):
    num=int(input('how many bugs did you collect today: '))
    total = total + num
print ('Total bugs collected: ', total)

