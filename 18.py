num = int(input("Enter the number = "))
for j in range(1,num):
    for i in range(1,num+1):
        if(j%2 != 0):
            if(i%2==0):
                print("1",end=" ")
            else:
                print("0",end=" ")
        else:
            if(i%2==0):
                print("0",end=" ")
            else:
                print("1",end=" ")

    print()
