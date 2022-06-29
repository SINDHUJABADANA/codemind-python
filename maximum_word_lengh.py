n=input()
n=n.split()
s=[]
for i in n:
    i=str(i)
    s.append(len(i))
print(max(s))