
#Write a program that asks the user to enter a
#store's sales for each day of the week.
#The amounts should be stored in a list.
#Use a loop to calculate the total sales for the week and display the result.
days=['Monday','Tuesday','Wednsday','Thursday',\
            'Friday','Saturday','Sunday']
sales = [0]*7
total = 0
for i in range (len(days)):
    sales[i]=float(input(f'Enter sales for {days[i]}: $'))
    total = total + sales[i]

print(f'Total sales for the week : ${total}')

for x in range (len(days)):
    print(f'{days[x]} sales: {sales[x]}')
