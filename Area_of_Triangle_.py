import math
a,b,c=map(int,input().split())
s=(a+b+c)/2
m=s*(s-a)*(s-b)*(s-c)
a=math.sqrt(m)
print('%.2f'%a)