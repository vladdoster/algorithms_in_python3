# Asked at Air Worldwide

# Write a function that  performs a combination
# ex 1. factorial(4) = 24
# ex 2. factorial(5) = 120
# ex 3. factorial(1) = 1

# Recursive approach
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
