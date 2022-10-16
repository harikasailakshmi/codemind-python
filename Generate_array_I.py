a=int(input())
x=list(map(int,input().split()))
z=[]
for i in range(0,a-1,2):
    for j in range(x[i+1]):
        z.append(x[i])
print(*z)
        