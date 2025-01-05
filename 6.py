num = int(input("Enter the number = "))
ch=1
for i in range(num,0,-1):
    for j in range(0,num):
        print(ch,end=" ")
        ch+=1
    print()