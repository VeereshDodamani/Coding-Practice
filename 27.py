print("Way-1")
def fib(n):
    if n==0:
        return 0
    if n==1:
        return 1
        
    return fib(n-2)+fib(n-1)

n = int(input("Enter number for Fibonacci series: "))
print(f"The {n}th Fibonacci number is: {fib(n)}")
