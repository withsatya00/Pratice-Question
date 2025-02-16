#2. Write a python program to calculate the alternating sum of square of digit of a given number. 
# Starting from the leftmost digit, square each digit and alternating between adding and subtracting the result.
# Without converting string.

#string method
'''import math
num=input()
temp=num
even=sum([pow(int(dig),2)for dig in num[1::2]])
odd=sum([pow(int(dig),2) for dig in num[::2]])
print(odd-even)'''



#integer method
n=int(input())
x=[];y=[]
while n>0:
    x.append((n%10)**2)
    n=n//10
    
for index in range(len(x)-1,-1,-1):
    y.append(x[index])
pos=1;sum=0
for i in y:
    if pos&1:
        sum=sum+i
    else:
        sum=sum-i
    pos=pos+1
print(sum)
    
    
#using string method
'''n=int(input())
l=[]
while n>0:
    l.insert(0,(n%10)**2)
    n=n//10
ans=0;pos=1
for index in l:
    ans=ans+index if pos&1 else ans-index
    pos=pos+1
print(ans)'''
    
    


