#45 poena na Petlji
m = sorted(list(map(int,input().split()))+list(map(int,input().split())))
if len(m)%2==0:
    print((m[len(m)//2]+m[len(m)//2-1])/2)
else:
    print(m[len(m)//2])
