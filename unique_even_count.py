n=int(input())
a=list(map(int,input().split()))
b=set(a)
c=0
for j in b:
    if j%2==0:
        c+=1
print(c)