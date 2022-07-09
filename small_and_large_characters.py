s=input()
a=list(s.split())
for i in a:
    ma='A'
    mi='z'
    for j in i:
        if j!=' ':
            if ord(j)>ord(ma):
                ma=j
            if ord(j)<ord(mi):
                mi=j
    print(mi,ma,end=" ")

