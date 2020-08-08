#Made by Mohit Patil
#08/08/2020
#Find Armstrong Number

n=int(input("Enter the Number:"))
m=n
sum=0
while n!=0:
    a=n%10
    n=n//10
    sum=sum+(a**3)
if(sum==m):
    print(str(m)+" is Armstrong")
else:
    print(str(m)+" is Not Armstrong")
    
    
