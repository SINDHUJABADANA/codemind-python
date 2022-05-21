num=int(input())
sum=0
k=num
while num:
    rem=num%10
    num=num//10
    sum=sum+rem
if k%sum==0:
    print('True')
else:
    print('False')