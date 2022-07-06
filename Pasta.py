n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
s=0
for i in b:
    if i in a:
        a.remove(i)
        s+=1
if s==m:
    print("Yes")
else:
    print("No")