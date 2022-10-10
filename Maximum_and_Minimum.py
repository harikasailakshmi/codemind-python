n=int(input())
a=list(map(int,input().split()))
z=set(a)
k=[]
for i in z:
    if a.count(i)==i:
        k.append(i)
if k==[]:
    print(-1)
else:
    print(min(k),max(k))