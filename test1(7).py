time=input()
time=time+"."
a=0
b=0
out=0
mo=0
month_day=0
def year(int):
    p=0
    if int%4==0 and int%100!=0:
        p=p+1
    elif int%400==0:
        p=p+1
    return bool(p)

#************************************************************
for i in range(len(time)):
    if time[i] != ".":
        a=a*10+int(time[i])
    else:
        b=b+1;

    if b==1:
        mo=year(a)
        for u in range(a-2000):
            a=a-1
            y=year(a)
            if y:
                out=out+366
            else:
                out=out+365
    if a==2000:
        a=0
        b=b+1           
    if b==3:
        b=b+1
        month=1
        month_day=a
        for t in range(12):
            if a==month:
                a=0
                break
            else:
                if month==1 or 3 or 5 or 7 or 8 or 10:
                    out=out+31
                if month==2 and mo:
                    out=out+29
                else:
                    out=out+28
                if month==4 or 6 or 9 or 11:
                    out=out+30
            month=month+1
    if b==5:
        out=out+a-1
print(out)