"""A code to test recursion speed and breaking point versus a while loop point of reference."""
import datetime
def recursion(x):
    """Recursively counts down from the input number."""
    print(x)
    if x > 0:
        recursion(x - 1)
    print(x)
    
def while_loop(x):
    """Uses a while loop to count down from the input number."""
    while x > 0:
        x -= 1


if __name__ == '__main__':  
    number = 10
    #run this code with increasingly high numbers.
    #10, 100, 1000, etc
    timeA = datetime.datetime.now()
    # while_loop(number)
    timeB = datetime.datetime.now()
    print('while loop took ', timeB - timeA)
    timeA = datetime.datetime.now()
    recursion(number)
    timeB = datetime.datetime.now()
    print('recursion took ', timeB - timeA)