num=int(input())
rev=0
temp=num
while num:
    rem=num%10
    rev=rev*10+rem
    num=num//10
if temp==rev:
    print('True')
else:
    print('False')
    