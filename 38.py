num = int(input("Enter the number = "))
for i in range(num,0,-1):
    m=num
    for j in range(i,num+1):
        print(m,end=" ")
        m-=1
    print()