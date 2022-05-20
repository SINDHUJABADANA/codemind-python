n=int(input())
s=n*n
rev=0
while n:
    rem=n%10
    rev=rev*10+rem
    n=n//10
q=rev*rev
rev1=0
while q:
    rem1=q%10
    rev1=rev1*10+rem1
    q=q//10
if rev1==s:
    print("True")
else:
    print('False')
    