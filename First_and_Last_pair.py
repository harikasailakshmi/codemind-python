n=int(input())
a=list(map(int,input().split()))
k=[]
c=0
j=1
m=[]
x=0
for i in range((n-1),((n-1)//2)-1,-1):
    m.append(a[i])
for i in range(1,n+1):
    if i%2!=0:
        k.append(a[c])
        c+=1
    else:
        k.append(m[x])
        x+=1
if n%2!=0:
    k.append(0)
print(*k)