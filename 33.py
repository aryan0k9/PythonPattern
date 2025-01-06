num = int(input("Enter the number = "))
for i in range(num,0,-1):
    m=0
    for j in range(num):
        print(chr(64+m+i),end=" ")
        m+=5
    print()