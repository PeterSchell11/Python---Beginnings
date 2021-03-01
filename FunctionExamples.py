#Functions

def message():
    print('I am Arthur')
    print ('King of the britons')

message()
message()
    #function is being called


def greet():
    print('hello everybody')
def greetAgain():
    print('hello again')

greet()
greetAgain()

#function calling a function within it
def main():
    print('i have a message for you')
    message()
    print('goodbye')

main()