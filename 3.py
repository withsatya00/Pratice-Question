'''taking input form teh user
check the how many digit are divisible by 3
and how many digit are divisible by 5
and find absoulete difference betwwen them'''

'''n=int(input())
count1,count2=0,0
while n>0:
    digit=(n%10)
    if digit % 3==0:
        count1=count1+1
    elif digit % 5==0:
        count2=count2+1
    n=n//10


print(count2-count1)'''
    
    
n=int(input())
ans=0
while n>0:
    digit=(n%10)
    if digit % 3==0:
        ans=ans+1
    elif digit % 5==0:
        ans=ans-1
    n=n//10
print(ans if ans >0 else -ans) 
    