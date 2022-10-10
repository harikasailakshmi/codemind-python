n=int(input())
a=list(map(int,input().split()))
z=set(a)
k=0
c=0
for i in z:
    if a.count(i)==i:
        
        k+=i
        c+=1
if c==0:
    print(-1)
else:
    print("%.2f"%(k/c))
    