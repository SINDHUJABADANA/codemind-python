a=int(input())
rev=0
while(1):
    if a%10!=0:
        break
    else:
        a//=10
c=0
while(a<0):
    a*=-1
    c+=1
while(a>0):
    r=a%10
    rev=rev*10+r
    a=a//10
if c>0:
    print(-1*rev)
else:
    print(rev)

    