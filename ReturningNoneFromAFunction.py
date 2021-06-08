#ReturningNoneFromAFunction
    #Without return you can call function but not assign output to a function

def print_something(s):
    #return s
    print('Printing::', s)
    
#variable= print_something("I am still here")
#print(variable)
output = print_something('Hi')
print(f'A function without return statement returns {output}')

##

def main():
    num1=int(input("Enter a number: "))
    num2=int(input("Enter another number: "))
    quotient= divide(num1,num2)
    
    if quotient is None:
        print('Cannot divide by zero.')
        
    else:
        print(f'{num1} divided by {num2} is {quotient}')
        
def divide(num1, num2):

    if num2 == 0:
        result = None
        
    else:
        result = num1 / num2
    return result

main()

#########################

def pay():
    hours=int(input("How many hours did you work this week? : "))
    payPerHour=float(input("what is your hourly rate?: "))
    
    if (hours>40):
        overtimeHours=hours-40
        overtimePay=overtimeHours*(payPerHour*1.5)
        regHours = hours-overtimeHours
        regPay = regHours*payPerHour
        totalPay = regPay+overtimePay
        return (regHours,regPay,overtimeHours,overtimePay,hours,totalPay)
        
    else:
        regPay=hours*payPerHour
        
        return (hours, regPay, None, None,hours,regPay)
        
hours,pay,OThours,OTpay,totalHours,totalPay=pay()
print(f'Regular Hours worked :  {hours} \nRegularPay : \t\t{pay}')
print(f'Overtime hours worked : {OThours} \nOvertime Pay : \t\t{OTpay}')
print(f'Total hours worked : \t{totalHours} \nTotal Pay : \t\t{totalPay}')