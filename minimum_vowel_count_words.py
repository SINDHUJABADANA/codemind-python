a=input()
a=a.split()
b=''
d=0
for i in a:
    i=str(i)
    c=0
    for j in i:
        if j in 'aeiouAEIOU':
            c+=1
    b=b+str(c)
for i in b:
    if i==min(b):
        d+=1
print(d)