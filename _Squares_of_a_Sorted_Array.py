n=int(input())
a=list(map(int,input().split()))
a=set(a)
b=[]
for i in a:
    b+=[i*i]
c=sorted(b)
for j in c:
    print(j,end=' ')