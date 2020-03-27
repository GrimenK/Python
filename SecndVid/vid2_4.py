userInp = int(input("Enter seat from 1 to 54: "))
if userInp <= 36:
    if userInp % 2 == 0:
        print("Seat is in upper compartment")
    else:
        print("Seat is in lower compartment")
else:
    if userInp % 2 == 0:
        print("Seat is upper")
    else:
        print("Seat is lower")
    
