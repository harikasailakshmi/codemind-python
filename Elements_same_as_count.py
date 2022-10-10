n=int(input())
a=list(map(int,input().split()))
z=[]
for i in a:
    if i not in z:
        z.append(i)
k=[]
for i in z:
    if a.count(i)==i:
        k.append(i)
if k==[]:
    print(-1)
else:
    print(*k)