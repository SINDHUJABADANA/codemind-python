num=int(input())
sum=0
temp=num
while temp:
    rem=temp%10
    pro=1
    for i in range(1, rem+1):
        pro=pro*i
    sum=sum+pro
    temp=temp//10
if num==sum:
    print('The number',num,'is a strong number')
else:
    print('The number',num,'is not a strong number')