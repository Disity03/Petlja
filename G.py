a,b= list(map(int,input().split())),list(map(int,input().split()))

if len(a)>len(b):
    c=list(a)
    for i in a:
        if i in b:
            c.remove(i)
            b.remove(i)
    print(c[0])
else:
    c=list(b)
    for i in b:
        if i in a:
            c.remove(i)
            a.remove(i)
    print(c[0])
