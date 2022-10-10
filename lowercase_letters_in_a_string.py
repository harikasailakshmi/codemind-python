a=input()
b=list(a.strip())
c=0
for i in b:
    if i>='a' and i<='z':
        
        c+=1
print(c)