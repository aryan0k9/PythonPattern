num = int(input("Enter the number = "))
m=0
for i in range(1,num):
    m=m+i
    n=m
    for j in range(i,0,-1):
        print(n,end=" ")
        if(n>1):
            n-=1
    print()