num = int(input("Enter the number = "))
m=1
for i in range(1,num*2,2):
    for j in range(1,num+1):
        print(i,end=" ")
        i+=2
    print()