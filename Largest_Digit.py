num=int(input())
l=0
while num:
    rem=num%10
    num=num//10
    if rem>l:
        l=rem
print(l)