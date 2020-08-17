import math

def printHello(x):
    for reps in range(0, x):
        print("hello")


def squareNumber(num):
    return num**2


def findFirstLetter(inputString):
    return inputString[0]


def getAreaCode(num):
    num = num.split('-')
    return num[0]


def reverseString(randomString):
    return randomString[::-1]


def addContact(name, age, number, contactBook):
    contactBook[name] = [name, age, number]


def main():
    y = 5
    a = 7
    randomString = "dsfasdaga"
    num = '905-999-9999'
    contactBook = {"person1": ["person1", "10", "111-111-1111"]}
    listOfContacts = [["person4", "40", "444-444-4444"], ["person5", "50", "555-555-5555"]]

    for person in range(0, len(listOfContacts)):
        addContact(listOfContacts[person][0], listOfContacts[person][1], listOfContacts[person][2], contactBook)

    b = 16
    print(math.sqrt(16))

if __name__ == "__main__":
    main()
