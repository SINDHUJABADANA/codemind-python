b=int(input())
ce=0
co=0
a=list(map(int,input().split()))
for i in a:
    if i%2==0:
        ce+=1
    if i%2!=0:
        co+=1
print(ce ,co)