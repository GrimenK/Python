p = 7
h = 12
userNumbers = []
sumNumbers = 0
multiplyNumbers = 1
counter = 0

while True:
    userNum = int(input("Enter your number: "))
    userNumbers.append(userNum)
    if (userNum == p or userNum == h):
        break

for i in userNumbers:
    if i<p:
        sumNumbers += i
    if i>h:
        multiplyNumbers *= i
    elif (i>p and i<h):
        counter += 1

print("Summary of numbers: ",sumNumbers)
print("Multiply of numbers: ",multiplyNumbers)
print("Count of elements between P and H: ",counter)
