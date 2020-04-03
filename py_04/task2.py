userNum = list(map(int,input("Enter 10 numbers: ").split()))
print("Numbers", userNum)
counter = 0

for i in userNum:
    if i%5 == 0:
        counter += 1
print("Numbers dividing by 5: ", counter)
