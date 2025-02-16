'''taking +vs input from user
check if the sum of all digit divisible by product of digit
if product is zero return product is zero 
'''

n=int(input())
sum,product=0,1
while n>0:
    digit=n%10
    product=product*digit
    sum=sum+1
    n=n//10

'''print_=''
if product==0:
    print_='Product is zero'
elif sum%product==0:
    print_='Yes'
elif sum % product !=0:
    print_='No'
print(print_)'''


print("product is zero" if product==0 else 'yes' if sum%product==0 else 'No')
