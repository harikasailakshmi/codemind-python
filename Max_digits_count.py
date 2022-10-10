n=int(input())
a=list(input().split())
z=map(int,a)
k=len(str(max(z)))
c=0
for i in a:
    if k==len(i):
        c+=1
print(c)
