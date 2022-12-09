def prime(a):
    c=0
    for i in range(1,(a//2)+1):
        if a%i==0:
            c+=1
    if c==1:
        return 1
    else:
        return 0
n=int(input())
f=0
for i in range(1,n+1):
    for j in range(1,n+1):
        if i!=j:
            if(i*j==n):
               k=prime(i)
               l=prime(j)
               if(k==1 and l==1):
                   print(i,j)
                   f=1
    if f==1:
        break
if(f==0):
    print("-1")
