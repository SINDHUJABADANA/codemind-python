str=input()
sum=0
for i in range(len(str)):
    if str[i]>='0' and str[i]<='9':
        sum=sum+int(str[i])
print(sum)