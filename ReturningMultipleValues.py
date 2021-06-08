#ReturningMultipleValues

def getName():
    first=input("Enter first name: ")
    last=input("Enter last name: ")

    return first, last
print(getName())


def weatherForToday():
    day=input("What day is it: ")
    weather=input("Whats the weather like: ")

    return day, weather
d , w = weatherForToday()
print(f'Today is {d} and the weather is {w}')