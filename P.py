brojLK, JMBG, pol, diLK = input(),input(),input(),input()
pk=dk=tk=ck=0
for i in range(len(brojLK)):
    c=int(brojLK[i])
    if i%3==0:
        pk+=7*c
    if i%3==1:
        pk+=3*c
    if i%3==2:
        pk+=c
pk = str(pk%10)

dr= JMBG[5]+JMBG[6]+JMBG[2]+JMBG[3]+JMBG[0]+JMBG[1]
for i in range(6):
    c=int(dr[i])
    if i%3==0:
        dk+=7*c
    if i%3==1:
        dk+=3*c
    if i%3==2:
        dk+=c
dk= str(dk%10)

for i in range(len(diLK)):
    c=int(diLK[i])
    if i%3==0:
        tk+=7*c
    if i%3==1:
        tk+=3*c
    if i%3==2:
        tk+=c
tk = str(tk%10)

pred= "IDSRB"+brojLK+pk+JMBG+"<<"
dred= dr+dk+pol+diLK+tk+"SRB<<<<<<<<<<<"

obar=""

for i in range(len(pred)):
    if pred[i].isdigit():
        obar+=pred[i]
    elif pred[i]=="<":
        obar+="0"
for i in range(len(dred)):
    if dred[i].isdigit():
        obar+=dred[i]
    elif dred[i]=="<":
        obar+="0"
for i in range(len(obar)):
    c=int(obar[i])
    if i%3==0:
        ck+=7*c
    if i%3==1:
        ck+=3*c
    if i%3==2:
        ck+=c
ck=str(ck%10)

dred+=ck
print(pred)
print(dred)
