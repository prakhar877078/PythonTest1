# Program to find factorial of a number

factorial=1

num=10

if num<0:
    print("Factorial does not exist for negative numbers")
elif num==1:
    print("Factorial of 0 is 1")
else:
    for i in range(1,num+1):
        factorial=factorial*i
    print("The factorial of",num,"is",factorial)