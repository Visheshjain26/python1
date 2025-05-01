age=int(input("enter age"))
if age<=0:
    print("enter valid no.")
elif age<18:
    print("minor")
else:
    print("major")