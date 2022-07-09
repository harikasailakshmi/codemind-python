s=input()
mic=mac=0
ma='A'
mi='z'
for i in s:
    if i!=' ':
        if ord(i)>ord(ma):
            ma=i
        if ord(i)<ord(mi):
            mi=i
for i in s:
    if ma==i:
        mac+=1
    if mi==i:
        mic+=1
print(mi,mic,ma,mac)