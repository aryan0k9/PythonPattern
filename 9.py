num = int(input("Enter the number = "))
for i in range(1,num+1):
    for j in range(1,num+1):
        k= i*j
        if(k>9):
            print(k,end=" ")
        else:
            print(f' {k}',end=" ")
    print()