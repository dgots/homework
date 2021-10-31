a=int(input())
p=0
for i in range(int(a**0.5)):
    if a%(i+2)==0:
        p=p+1
p=bool(not p)
print(p)