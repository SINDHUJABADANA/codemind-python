n=input()
n=n.split()
c=0
for i in n:
    i=str(i)
    for j in range(len(i)):
        if j<=len(i)-1-j:
            if (i[j] in "AEIOUaeiou" and i[len(i)-1-j] not in "AEIOUaeiou ") or (i[j] not in "AEIOUaeiou " and i[len(i)-1-j]  in "AEIOUaeiou"):
                c+=1
print(c)