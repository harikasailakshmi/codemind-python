n=input()
n=n.lower()
a=list(n)
v=['a','e','i','o','u']
c=0
for i in a:
    if i in v:
        c+=1
print(c)