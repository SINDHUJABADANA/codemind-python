a=int(input())
c=0
rev=0
temp=a*a
n=len(str(a))
while(temp):
    rem=temp%10
    rev=rev*10+rem
    c+=1
    if c==n:
        break
    temp=temp//10
rev=str(rev)
rev=rev[::-1]
if int(rev)==a:
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")
    