def prime(n):
    c=0
    for i in range(1,(n//2)+1):
        if n%i==0:
            c+=1
    if(c==1):
        return 1
    else:
        return 0
n=int(input())
if(prime(n)==1):
    temp=n
    c1=0
    while(temp>0):
        rem=temp%10
        if(prime(rem)==1):
            c1+=1
        temp=temp//10
    if(c1==len(str(n))):
        print("Mega Prime")
    else:
        print("Not Mega Prime")
else:
    print("Not Mega Prime")
            
