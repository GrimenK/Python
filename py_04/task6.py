userNumbers = []
flag = 0
percentagePositive = 0
percentageNegative = 0
counter = 0

while flag<1:
    userNum = int(input("Enter your number: "))
    userNumbers.append(userNum)
    if userNum == 0:
        flag += 1
        del userNumbers[-1]
print(userNumbers)

for i in userNumbers:
    if i<0:
        counter += 1
        percentageNegative = counter / len(userNumbers) * 100
        percentagePositive = (len(userNumbers)-counter) / len(userNumbers) * 100
print("Відсоток від'ємних чисел: {}%,Відсоток додатних чисел:{}%".format(int(percentageNegative),int(percentagePositive)))
