v1=list(input())
d2=len(v1)
new3=''
for l in range (0,d2,2):
    v1[l],v1[l+1]=v1[l+1],v1[l]
print(*v1,sep='')
