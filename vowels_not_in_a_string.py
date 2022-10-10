a=input()
b=list(a.strip())
c=0
v=['a','e','i','o','u']
z=[]
for i in b:
    if i in v:
        z.append(i)
for i in v:
    if i not in z:
        c=1
        print(i,end=' ')
if c==0:
    print(0)