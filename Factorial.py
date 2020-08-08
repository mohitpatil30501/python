#Made by Mohit Patil.
#08/08/2020
#Find factorial of given number

fact=1
n=int(input("Enter number:"))
while(n>=1):
    fact=fact*n
    n-=1
print("Factorial: "+str(fact))
