num=int(input())
ce=0
co=0
while num:
    rem=num%10
    if rem%2==0:
        ce+=1
    if rem%2!=0:
        co+=1
    num=num//10
if ce>=1 and co==0:
    print('Even')
if ce==0 and co>=1:
    print('Odd')
if ce>=1 and co>=1:
    print('Mixed')