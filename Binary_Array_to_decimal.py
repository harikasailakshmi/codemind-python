n=int(input())
a=list(map(int,input().split()))
z=0
e=0
for i in range(n-1,-1,-1):
    z=z+(2**e)*a[i]
    e+=1
print(z)
    