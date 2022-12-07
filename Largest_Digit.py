n=int(input())
l=[]
while(n):
    rem=n%10
    l.append(rem)
    n=n//10
print(max(l))