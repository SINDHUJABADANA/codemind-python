t=int(input())
for i in range(1,t+1):
    num=int(input())
    rev=0
    temp=num
    while temp:
        rem=temp%10
        rev=rev*10+rem
        temp=temp//10
    if num==rev:
        print('True')
    else:
        print('False')