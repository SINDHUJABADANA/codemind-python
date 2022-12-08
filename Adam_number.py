def reverse(a):
    rev=0
    while(a>0):
        rem=a%10
        rev=rev*10+rem
        a=a//10
    return rev
n=int(input())
s1=n*n
n2=reverse(n)
s2=n2*n2
if s1==reverse(s2):
    print("True")
else:
    print("False")
