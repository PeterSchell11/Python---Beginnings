#Nested Loops
  
num_students = int(input('How many students do you have? '))

num_test_scores = int(input('How many test scores per student? '))

for student in range(num_students):
    
    total = 0.0

 #initially your student variable is 0 when you are printing you want it to 
#appear as student number 1 so you are adding 1 to your student variable
    
    print(f'Student number {student+1 }')
    print('-----------------')

    for test_num in range(num_test_scores):
        
        print(f'Test number {test_num + 1}', end='')
        score = float(input(': '))
        total += score
        average=total/num_test_scores
    
    print(f'The average for student number {student + 1} '
          f'is: {average:.1f}')
    print()

#############################

numFiles = int(input('How many files do you have? '))

numNum = int(input('How many numbers in each file? '))

for files in range(numFiles):
    
    total = 0.0

 
    print(f'File number {files+1 }')
    print('-----------------')

    for num in range(numNum):
        
        print(f' numbers in file {num + 1}', end='')
        score = float(input(': '))
        total += score
        average=total/numNum
    
    print(f'The average in file number {files + 1} '
          f'is: {average:.1f}')
    print()