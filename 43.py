num = int(input("Enter the number = "))
m=1
for i in range(1,num*2):
    if(i%2!=0):
        for j in range(i,0,-2):
            if(i<=9):
                print("",i,end=" ")
            else:
                print(i,end=" ")
            i+=2
        print()
