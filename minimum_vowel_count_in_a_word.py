x=input()
k=x.split()
s=[]
for i in k:
    z=list(i)
    c=0
    for i in z:
        if i in 'aeiouAEIOU':
            c+=1
    s.append(c)
h=min(s)
print(h)