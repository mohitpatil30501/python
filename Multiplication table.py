#Made by Mohit Patil.
#08/08/2020
#Multiplication Table of given number

n=int(input("Enter number:"))
print("\nTable of "+str(n)) 
for i in range(1,11):
    print(str(n)+" X "+str(i)+" = "+str(n*i))
