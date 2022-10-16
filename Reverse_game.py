n=int(input())
a=list(input().split())
z=[]
for i in a:
    if int(i)<0:
        z.append((-1)*(int(i[::-1])))
    else:
        z.append(int(i[::-1]))
print(*z)