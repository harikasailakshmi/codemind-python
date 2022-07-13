x=input()
y=input()
x=x.lower()
y=y.lower()
x=x.split()
y=y.split()
c=0
for i in x:
    for j in y:
        if i==j:
            c+=1
print(c)
            
        