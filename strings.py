
#

count=0

myString=input("Enter a sentence: ")

#count characters
for ch in myString:
    if ch=='T' or ch=='t':
        count+=1

print(f'The letter T appears {count} time(s)')

#Indexing

my_string='Roses are red'
ch=my_string[0]#string index are 0 - 12 ; -1 for last index
print(ch)
print(my_string[0],my_string[1],my_string[-1],my_string[-3])


#index error exceptions

#city='Boston'
#print(city[6])
#will cause an error- index range 0-5

##city = 'Boston'
##index=0
##while index<7:
##    print(city[index])
##    index+=1
#will cause an error- index range 0-5



#The len Function

city='Boston'
size=len(city)
print(size)
      
index=0
while index<len(city):
    print(city[index])
    index+=1

#string concatenation

message = 'Hello ' + 'world'
print(message)

letters='abc'
letters+='def'
print(letters)

#strings are immutable

#string slicing

mystring='abcdefg'

print(mystring[1:4])
print(mystring[-3:])
print(mystring[0:7:2])




#Last 2 digits of first name
firstName=input('Enter first name: ')
#first 3 digits of last name
lastName=input('Enter last name: ')
#last 4 digits of accountnumber
accountNum=input('Enter account number: ')

acctLogin = firstName[-2:]+lastName[:3]+accountNum[-4:]

print(f'Acount login username : {acctLogin}')


text = "I love sunny and warm weather"
if 'like' not in text:
    print("The String 'like' was not in the text")
else:
    print("The String 'like' was in the text")



#String Methods

string=input('Enter string')

if string.isalpha():
    print(f'{string} is alphabetical')
    if string.islower():
        print(f'{string} is all lower')

else:
    print('Includes letters that are not in the alphabet')

text = "I love rainy days and I love cold weather"
atext='I '#need space after
count = text.count(atext)
print(count)


#repitition statment
sym ='*'
total=10
for i in range(1,11):
    print(sym*i)

#splitting a string

myString = "one two three four"
wordList=myString.split()
print(wordList)

string = ' 1/2/3/4/5'
numsList=string.split('/')
print(numsList)

date = '11/18/2020'
    
numList=date.split('/')
month= ['Jan', 'Feb','Mar','Apr','May','June','July','Aug','Sep','Oct',\
        'Nov','Dec']
index = int(numList[0])-1

print(f'Month : {month[index]}')
print(f'Day : {numList[1]}')
print(f'Year : {numList[2]}')




