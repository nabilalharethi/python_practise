
def nth_number(n):
    lis =[]
    for x in range(1,n+1):
        lis.append(x)
    
    print(*lis,sep="")


n= int(input("Enter a number:"))

nth_number(n)