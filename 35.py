num = int(input("Enter the number = "))
m=1
for i in range(num,0,-1):
    for j in range(num+1,i,-1):
        print(m,end=" ")
    m+=1
    print()