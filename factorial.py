def factorial(n):
    fact = 1 
    if n<0:
        return ("Invalid Input !!")
    elif n==0:
        return 1
    else:
        while n>=1:
            fact *= n
            n -= 1
        return fact


num = int(input("Enter a number to calculate its factorial : "))
res=factorial(num)
print("Factorial of ", num, "is = ",res)
