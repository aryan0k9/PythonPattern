num = int(input("Enter the number = "))
for i in range(num):
    m=0
    for j in range(num):
        print(chr(65+i+m),end=" ")
        m+=5
    print()