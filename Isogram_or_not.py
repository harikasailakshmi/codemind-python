x=input()
z=0
for i in x:
    c=0
    for j in x:
        if i==j:
            c+=1
    if c>1:
        z+=1
if z==0:
    print("True")
else:
    print("False")