num = int(input("Enter the number = "))
for i in range(num):
    for j in range(num,0,-1):
        print(chr(64+j),end=" ")
    print()