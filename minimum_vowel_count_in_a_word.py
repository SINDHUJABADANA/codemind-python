a=input()
a=a.split()
s=[]
for i in a:
    i=str(i)
    c=0
    for j in i:
        if j in 'aeiouAEIOU':
            c+=1
    s.append(c)
print(min(s))