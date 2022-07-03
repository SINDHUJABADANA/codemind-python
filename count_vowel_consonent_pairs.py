n=input()
c=0
for i in range(len(n)):
    if i<=len(n)-1-i:
        if (n[i] in "AEIOUaeiou" and n[len(n)-1-i] not in "AEIOUaeiou ") or (n[i] not in "AEIOUaeiou " and n[len(n)-1-i]  in "AEIOUaeiou"):
            c+=1
print(c)