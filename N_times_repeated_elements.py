n=int(input())
a=list(map(int,input().split()))
m=int(input())
z=[]
o=0
for i in a:
    if i not in z:
        z.append(i)
for i in z:
    c=0
    for j in a:
        if i==j:
            c+=1
    if c==m:
        o=1
        print(i,end=" ")
if o==0:
    print(-1)
    