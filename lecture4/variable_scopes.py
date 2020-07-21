# function and variable scopes

def squareNumber(n):
    return n**2


users = 4  # this variable is out of main's scope

def triple(n):
    bananas = 5  # this variable is also out of main's scope
    bananas *= 3
    print(bananas)


def main():
    users = 3
    square_users = squareNumber(users)
    # print(bananas)  #  uncomment this and you'll get an error. The variable bananas doesn't exist in this scope
    print(square_users)  # the users variable from the main method scope is used


if __name__ == "__main__":
    main()
