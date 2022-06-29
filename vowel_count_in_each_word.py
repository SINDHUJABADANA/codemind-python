a=input()
a=a.split()
for i in a:
    i=str(i)
    c=0
    for j in i:
        if j in 'aeiouAEIOU':
            c+=1
    print(c,end=' ')
    