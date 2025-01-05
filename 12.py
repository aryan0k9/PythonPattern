num = int(input("Enter the number = "))

for i in range(1,num+1):
    ch = i
    for j in range(1,num+1):
        if(ch > 9):
            print(ch,end=" ")
        else:
            print(f' {ch}',end=" ")
        ch+=5
    print()