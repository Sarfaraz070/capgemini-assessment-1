d={}
l=list(input().split())
for i in l:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
print(d)


