msg = "Oleg Grimenkov"
print(msg)
hello = "Hello"
print(hello + msg)
hello = hello + " "
print(hello + msg)
msg = msg[0:5] + "Igorevich " + msg[5:14]
print(msg)

s = 'colorless'
s = s[0:4] + 'u' + s[4:9]
print(s)

listLet = "dish-es, run-ning, fight-ing"
for i in listLet:
    if i == '-':
        afix = listLet.find('-')
        listLet = listLet[:afix] + listLet[afix+1:]
    else:
        continue
print(listLet)
