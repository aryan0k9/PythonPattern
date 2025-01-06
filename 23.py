num = int(input("Enter the number = "))
for i in range(1,num+1):
    for j in range(num):
        if(i%2!=0):
            print("1",end=" ")
        else:
            print("0",end=" ")
    print()