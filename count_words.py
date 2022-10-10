a=input()
a=a.lower()
b=a.split()
v=['a','e','i','o','u']
c=0
for i in b:
    if i[0] in v:
        if i[len(i)-1] not in v:
            c+=1
print(c)