#43 poena na Petlji
x= list(map(int,input().split()))
ma=max(x)
mi=ma
for i in range(x.index(mi),0,-1):
    if x[i]<mi:
        mi=x[i]
print(ma-mi)
