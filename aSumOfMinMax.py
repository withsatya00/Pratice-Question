n=int(input())
l=[]
for i in range(0,n):
    m=int(input())
    l.append(m)
print(l)

if n==1:
    print(l[0])
if l[0]>l[1]:
    min=l[1]
    max=l[0]
else:
    min=l[0]
    max=l[1]
for i in range(2,n):
    if l[i]>max:
        max=l[i]
    elif l[i]<min:
        min=l[i]
print(min+max)