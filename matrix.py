size=int(input("enter size:"))
for row in range(0,size):
    for col in range(0,size):
        if(row==col):
            print("1")
        else:
            print("0")   

