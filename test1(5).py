a,b=map(int,input().split())
c=0
s=0
for i in range(b):
    c=c*10+a
    s=s+c
print(s)