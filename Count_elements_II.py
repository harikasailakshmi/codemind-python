a,b=map(int,input().split())
x=list(map(int,input().split()))
y=list(map(int,input().split()))
c=set(x+y)
d=0
for i in c:
    if (i in x and i not in y) or (i not in x and i in y):
        d+=1
print(d)