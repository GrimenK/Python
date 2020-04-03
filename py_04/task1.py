import random

randNb = random.randint(1,100)

guess = 0
while (guess < 10):
    userNum = int(input("Enter your number: "))
    if userNum < randNb:
        print("Wrong number! Try larger number")
    elif userNum > randNb:
        print("Wrong number! Try smaller number")
    guess += 1
if userNum == randNb:
    print("Yaaay! You got it")
else:
    print("You tried :(")
