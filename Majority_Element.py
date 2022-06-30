n=int(input())
a=list(map(int,input().split()))
b=[]
for i in a:
    b+=[a.count(i)]
c=max(b)
for j in a:
    if a.count(j)==c:
        print(j)
        break