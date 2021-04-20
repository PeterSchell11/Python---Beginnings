

month = {'January':31, 'February':28, 'March':31, 'April':30, 'May':31,
         'June':30, 'July':31,'August':31,'September':30, 'October':31,
         'November':30, 'December':31}
for i in month:
    if month[i] == 31:
        print(i)


dict1 = {1:10,2:20}
dict2 = {3:30,4:40}
dict3 = {5:50,6:60}

dict4 = dict1
dict4.update(dict2)
dict4.update(dict3)

print(dict4)


        
def checkKey(dict, key):

    if key in dict:
        print("Present, ",end=" ")
        print("value = ", dict[key])
    else:
        print("Not Present")

dict = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
key = 5
checkKey(dict, key)

key = 9
checkKey(dict, key)
