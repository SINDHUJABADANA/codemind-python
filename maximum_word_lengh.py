n=input()
n=n.split()
max=0
for i in n:
    i=str(i)
    if(max<len(i)):
        max=len(i)
print(max)