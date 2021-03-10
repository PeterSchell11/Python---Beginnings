#Lists
    #A list is collection which which is ordered and changeable
    #written with square brackets[]

thisList = ["apple", "banana", "cherry"]
print (thisList)

    #"" '' makes no difference ; will print the same
food = ['muffin', 'chips', 'coke']


    #Repitation Operator
        # symbol *

value = [1,2,3,4]*5
print(value)

#iterating over a List with the for loop
for x in [1,2,3,4,5]:
    print(x)



#positive indexing and negative indexing
myList = [4,21.2,'hi']
print (myList)
print (myList[0])#prints first on the list
print (myList[1])#
print (myList[2])#prints second on the list
print (myList[-1])#prints last item on the list
print (myList[-2])#prints second on the list
print (myList[-3])#prints third last item on the list


#List length
print(len(myList))#prints number of items in list

#using loop to iterate by index over list
fruits =['apple','banana','cherry']
for index in range (len(fruits)):
    print (fruits[index])
    
#Lists are Mutable
    #elements are changable

numbers=[1,2,3,4]
print (numbers)
numbers[0]=99
numbers[-1]=12
print(numbers)

    #if you want to fill list with indexing, you need to creat list first

nums=[0]*5
print(nums)
for index in range(len(nums)):
    nums[index]=float(input('enter number '))
print (nums)

#combining two lists

list1=[1,2,3]
list2=[4,5,6]
list3=list1+list2
print(list3)
