num = int(input("Enter the number = "))
for i in range(num):
    for j in range(1,num+1):
        print(chr(64+j),end=" ")
    print()