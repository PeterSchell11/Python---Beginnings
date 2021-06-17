

month=['Jan','Feb','Mar','Apr' , 'May','June', 'July','Aug','Sep','Oct','Nov','Dec']

rainfall=[0]*12
total=0
for index in range (len(rainfall)):
    rainfall[index]=float(input(f'monthly rainfall for {month[index]}: '))
    total+=rainfall[index]

average = total/(len(rainfall))

print(f'\ntotal rainfall: {total}')
print(f'Average rainfall: {average}')

for i in range (len(rainfall)):
    if rainfall[i]==min(rainfall): 
        print(f'Min rainfall {min(rainfall)} inch(es) in {month[i]}')
    if rainfall[i]==max(rainfall): 
        print(f'Max rainfall {max(rainfall)} inch(es) in {month[i]}')

    
#print(f'Min rainfall {min(rainfall)}')
#print(f'Max rainfall {max(rainfall)}')
