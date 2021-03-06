

#nested conditionals

x=10
y=10
if x<y:
    print('xis less than y')
else:
    if x>y:
        print('x is greater than y')
    else:
        print('x and y must be equal')

####################################

age = int(input("How old are you"))


graduate = bool (input("Have you Graduated? type 1 for true, leave blank for false"))
driver = bool(input("Do you have a drivers"))
if (age >17):
    print("greater than 17")
    if graduate:
        print("congratulations")
    if driver:
        print("be safe")
else:
    print("Good luck in school")

###################################

    day = int(input("enter the day of the month"))
month = int(input("enter month in numberically form"))
year = int(input("Enter year"))
year = year%100

if (day * month == year):
    print ("The day is magic")
else:
    print("the date is not magic")

####################################

#comparing Strings

name1='Mary'
name2='Mark'

if name1>name2:
    print('Mary is greater than Mark')
else:
    print('Mark is greater than Mary')
###############################

#logical operators
#"and"  "and or" ""

a=10
b=10
c=-10

if a>0 and b >0:
    print("the numbers are greater than 0")
if a>0 and b>0 and c>0:
    print("the numbers are greater than 0")
else:
    print("at least one number is less than or equals 0")

    

