num = int(input("Enter the number = "))
for j in range(num,0,-1):
    m=1
    for i in range(num+1,j,-1):
        print(m,end=" ")
        m+=1
    print()
