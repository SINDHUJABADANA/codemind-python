n=int(input())
a=list(map(int,input().split()))
b=[]
for i in a:
    if i not in b:
        b.append(i)
for j in b:
    print(j,end=' ')