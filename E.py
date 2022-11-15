#57 poena na Petlji
def opadajuc(x):
    pr=x%10
    x//=10
    while x>0:
        if x%10>pr:
            return False
        else:
            pr=x%10
            x//=10
    return True

x = int(input())
if opadajuc(x):
    print(x)
else:
    mo, vo ,m,v= None, None, x, x
    while mo==None:
        if opadajuc(m-1):
            mo=m-1
        else:
            m-=1
    while vo==None:
        if opadajuc(v+1):
            vo=v+1
        else:
            v+=1
    if (mo+vo)/2==x:
        print(str(mo)+" "+str(vo))
    elif abs(mo-x)<abs(vo-x):
        print(mo)
    else:
        print(vo)
