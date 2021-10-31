a=100
b=0
for i in range(899):
    if a==int(str(a)[0])**3+int(str(a)[1])**3+int(str(a)[2])**3:
        b=b+1
        if b==1:
            print(a,end="")
        else:
            print(",",end="")
            print(a,end="")
    a=a+1