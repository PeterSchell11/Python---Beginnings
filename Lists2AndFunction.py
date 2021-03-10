#Range of Indexes or Slicing
    #specify a range

st = ["apple", "banna" , "cherry", "orange", "kiwi", "melon", "mango"]
    #doesnt include second limit
print(st[2:5])
print(st[:4])
print(st[2:])

#range of negative indexes

print(st[-4:-1])

#Finding Items in list with an Operator

def main():
    productNums=['a893','b123','k381','c329']
    search=input('Enter a product number')

    if search in productNums:
        print(f'{search} was found')
    else:
        print(f'{search} was not found')

#list methods and useful built in functions
        
    #.append(index,item): adds items
numList = [1,2,3]
numList.append(4)
print(numList)

    #.insert(item) : adds an items at specified index
numList.insert(1,5)
print(numList)

    #.sort() - sorts numerically or alphabetically
numList.sort()
print(numList)

    #.remove(item) removes specified item
numList.remove(4)#can also do numList.remove(numlist[1])
print(numList)

    #reverse statement - 
numList.reverse()
print(numList)

    #the del statment - deletes specified 
del numList[0]#deletes index
print(numList)
#del numList[0:2] -deletes specified range ; list is not
#del numList - deletes list completely

    #.clear() - clear items from list but does not delete
numList.clear()
print (numList)

#the min and max funxtions
list1 = [4,3,6,7,8,56,57,45,7,876,346]
print(min(list1))
print(max(list1))

#copy lists
#cant do list1=list2 becasue changes in list1 will reflect on list2
#.copy()
list2=list1.copy()
print(list1)

#list
list3=list(list1)

#extend() method
list3.extend(list1)
print(list3)
list2.append(list1)#not the same
print(list2)

#practice
x=[1,2,3]
y=[4,5]
z=[4,2,3,1]

x.append(4)
x.extend(y)
z.sort()

print(x)
print(z)


animals = [ 'cat','dog','bird','tiger','squirrel']
animals1=animals.copy()
animals2=animals.copy()

animals.pop(1)
print(animals)

animals1.remove('tiger')
print(animals1)

del animals2[0:3]
print(animals2)



#pop() removes specific index (singular;will remove last items if not specied)
list12=[1,2,3,3,4,5]
list12.pop(3)
print(list12)
