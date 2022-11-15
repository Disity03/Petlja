niz= list(map(int,input().split()))
s=1
m=s
for i in range(len(niz)-1):
    if niz[i] > niz[i+1]:
        s+=1
        if i==len(niz)-2:
            if s>m:
                m=s
    else:
        if s>m:
            m=s
        s=1
print(m)
