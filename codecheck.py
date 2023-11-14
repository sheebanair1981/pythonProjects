#Write a Python function to find the factorial of a non-negative integer.
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
print(factorial(4))
