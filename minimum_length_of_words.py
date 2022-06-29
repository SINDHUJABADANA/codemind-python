n=input()
n=n.split()
min=100
for i in n:
    i=str(i)
    if(min>len(i)):
        min=len(i)
print(min)