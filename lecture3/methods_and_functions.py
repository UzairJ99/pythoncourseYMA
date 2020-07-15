# this method will print hello x times in our terminal
def printHello(x):
    for i in range(0, x):
        print('Hello')


# function that returns the n squared
def square(n):
    return n**2


# main method
def main():
    # call our printHello method
    printHello(5)
    # call our square function and save the returned value to x
    x = square(4)
    print(x)


# entry point to the program
if __name__ == "__main__":
    main()  # call the main method
