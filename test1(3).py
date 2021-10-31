year=input()
year=int(year)
p=0
if year%4==0 and year%100!=0:
    p=p+1
elif year%400==0:
    p=p+1
p=bool(p)
print(p)