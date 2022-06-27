str=input()
c=0
for i in range(len(str)):
    str=str.lower()
    if str[i]>='a' and str[i]<='z':
        c+=1
    if str[i]==' ':
        c+=1
print(c)