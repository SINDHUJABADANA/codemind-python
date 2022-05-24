n=int(input())
a=list(map(int,input().split()))
se=0
so=0
for i in range(len(a)):
    if i%2==0:
        se=se+a[i]
    elif i%2!=0:
        so=so+a[i]
if se==so:
    print('YES')
else:
    print('NO')