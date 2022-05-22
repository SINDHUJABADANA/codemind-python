num=int(input())
sum=0
sqr=num*num
while sqr!=0:
    rem=sqr%10
    sum=sum+rem
    sqr=sqr//10
if sum==num:
    print('Neon Number')
else:
    print('Not Neon Number')