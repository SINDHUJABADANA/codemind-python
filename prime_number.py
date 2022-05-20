def prime(a):
    for i in range(2,(a//2)+1):
        if a%i==0:
            return('not a prime')
    else:
        return('prime')
a=int(input())
print(prime(a))
