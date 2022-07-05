n=int(input())
a=list(map(int,input().split()))
k=[]
s=0
for i in a:
    if a.count(i)==1:
        k.append(i)
for i in k:
    m=max(k)
    s=1
if(s==1):
    print(m)
else:
    print("-1")