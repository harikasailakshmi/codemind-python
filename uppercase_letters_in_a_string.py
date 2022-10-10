a=input()
b=list(a.strip())
c=0
for i in b:
    if i>='A' and i<='Z':
        
        c+=1
print(c)