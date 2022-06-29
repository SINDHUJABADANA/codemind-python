n=int(input())
a=list(map(int,input().split()))
b=[]
c1=0
for i in a:
   c=len(str(i))
   b+=[c]
m=min(b)
for j in b:
    if j==m:
        c1+=1
print(c1)