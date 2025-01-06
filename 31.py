num = int(input("Enter the number = "))
for i in range(1,num+1):
    m = i
    for j in range(num):
        print(chr(64+m),end=" ")
        m+=1
    print()