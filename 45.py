num = int(input("Enter the number = "))
m=1
for i in range(num,0,-1):
    for j in range(i,num+1):
        print(m,end=" ")
        m+=2
    print()