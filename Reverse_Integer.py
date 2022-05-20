def rev(num):
    s=0
    while num:
        rem=num%10
        s=s*10+rem
        num=num//10
    return s
num=int(input())
if num>0:
    print(rev(num))
else:
    num*=-1
    print("-"+str(rev(num)))