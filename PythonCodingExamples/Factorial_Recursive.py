# Factorial of a number using recursive approach :

def factorial(n):
    return 1 if(n==0 or n==1) else n*factorial(n-1)

num=7
print("Factorial of",num,"is",factorial(num))