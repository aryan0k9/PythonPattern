num = int(input("Enter the number = "))
m=1
for i in range(num):
    for j in range(num):
        print(chr(64+m),end=" ")
        m+=1
    print()