s=input()
a=list(s.split())
for i in a:
    smax=smin=0
    ma='A'
    mi='z'
    for j in i:
        if ord(j)>ord(ma):
            ma=j
        if ord(j)<ord(mi):
            mi=j
    smax+=ord(ma)
    smin+=ord(mi)
    print(smax-smin,end=" ")