#Made by Mohit Patil.
#08/08/2020
#Fabonacci Series

f = 0
s = 1

n=int(input("Enter the Limit of terms:"))
print("First "+str(n)+" terms of Fibonacci series are:\n")

for i in range(0,n):
    if (i <= 1):
        nex = i
    else:
        nex = f + s
        f = s
        s = nex
    print(str(nex))
    
