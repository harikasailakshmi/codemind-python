s=input()
a=list(s.split())
ma='A'
mi='z'
for i in a[0]:
    if ord(i)<ord(mi):
        mi=i
for j in a[len(a)-1]:
    if ord(j)>ord(ma):
        ma=j
print(mi,ma,end=" ")
