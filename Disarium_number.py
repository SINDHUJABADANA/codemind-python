n=int(input())
temp=n
rev=0
c=0
s=0
while temp:
    rem=temp%10
    rev=rev*10+rem
    temp=temp//10
temp=rev
while temp:
    rem1=temp%10
    c+=1
    temp=temp//10
    x=rem1**c
    s=s+x
if s==n:
    print('True')
else:
    print('False')