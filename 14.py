num = int(input("Enter the number = "))
 
for i in range(num,0,-1):
    for j in range(num,0,-1):
        if(j==5):
            print(" ",i,end=" ")
        else:
            m=i+5
            if(m > 9):
                print(m,end=" ")
            else:
                print("",m,end=" ")
            i=m

    print()
