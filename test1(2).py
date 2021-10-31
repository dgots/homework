a,b,c=map(float,input().split())
p=(a+b+c)/2
rt=0;
if a*a+b*b==c*c:
    rt=rt+1
if a*a+c*c==b*b:
    rt=rt+1
if b*b+c*c==a*a:
    rt=rt+1
R=bool(rt)
C=int(a+b+c)
S=float((p*(p-a)*(p-b)*(p-c))**0.5)
print(C,S,R)