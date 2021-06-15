#program input number of clients, how many weeks each client was in the program,
#how much weight that client lost each week,
#and then output the everage each customer losst per week



numClients = int(input('How many clients do you have? '))

for client in range(numClients):
    
    total = 0.0

    print(f'Client number {client+1 }')
    print('-----------------')
    
    numWeeks = int(input('How many weeks was this client in a program? '))
    
    for week in range(numWeeks):
        
        print(f' Weight lost in week {week + 1}', end='')
        weekWeightLoss = float(input(': '))
        total += weekWeightLoss
        average=total/numWeeks
    
    print(f'The average in weight lost by  {client + 1} '
          f'is: {average:.1f}')
    