num = int(input("Enter the number = "))
for i in range(1,num+1):
    for j in range(0,i):
        print(i,end=" ")
        i+=1
    print()