userBytes = int(input("Enter bytes amount: "))

convKilob = userBytes / 1024 
convMegab = convKilob / 1024 

print("Kilobytes: {} Megabytes: {}".format(convKilob, convMegab))
