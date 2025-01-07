num = int(input("Enter the number = "))
for i in range(num,0,-1):
    m=2
    for j in range(i,num+1):
        print(m,end=" ")
        m+=2
    print()