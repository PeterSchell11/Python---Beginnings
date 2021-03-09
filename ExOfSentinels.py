#Sentinels

TAX_FACTOR = 0.0065

print('Enter the property lot number or enter 0 to end.')
lot = int(input('Lot number: '))

while lot != 0:
    value = float(input('Enter the property value: '))
    tax = value * TAX_FACTOR
    print(f'Property tax: ${tax:,.2f}')
    print('Enter the next lot number or enter 0 to end.')
    lot = int(input('Lot number: '))


#Sentinels

print('Enter the number of products sold or enter 0 to end.')
numPro = int(input('Products sold: '))

while numPro != 0:
    
    commish = 5 * numPro
    print("commission is :", commish)
    print('Enter new product price number or enter 0 to end.')
    numPro = int(input('new product price: '))