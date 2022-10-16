a,b=map(int,input().split())
x=list(map(int,input().split()))
y=list(map(int,input().split()))
z=[]
for i in (x+y):
    if i not in z:
        z.append(i)
d=[]
for i in z:
    if (i in x and i not in y) or (i not in x and i in y):
        d.append(i)
print(*d)