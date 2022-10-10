s=input()
k=s.split()
a=100000
for i in k:
    if a>len(i):
        a=len(i)
print(a)