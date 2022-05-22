t=int(input())
for i in range(1,t+1):
    num=int(input())
    for i in range(1,num+1):
        if num==i*i:
            print('True')
            break
    else:
        print('False')