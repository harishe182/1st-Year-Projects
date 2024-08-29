# This is the starter template for the week 1 participation assignment

# Input n: integer
# constraints: n > 0
# Output: nth Fibonacci number
# Examples:
# |  Input  |  Output  |
# |---------|----------|
# |    1    |     0    |
# |---------|----------|
# |    5    |     3    |
# |---------|----------|
# |   20    |   4181   |
# |---------|----------|
def fibonacciRecursive(m):
    if m <= 0:
        return 0
    if m == 1:
        return 0
    elif m == 2:
        return 1
    else:
        return fibonacciRecursive(m - 1) + fibonacciRecursive(m - 2)

m = int(input("Enter Number: "))
print(f"The {m}th Fibonacci number is: {fibonacciRecursive(m)}")


# Input n: integer
# constraints: n > 0, no recursion in implementation
# Output: nth Fibonacci number
# Examples:
# |  Input  |  Output  |
# |---------|----------|
# |    1    |     0    |
# |---------|----------|
# |    5    |     3    |
# |---------|----------|
# |   20    |   4181   |
# |---------|----------|
def fibonacciIterative(n):
    #checks constraints (n>0), as well as when its 1 or 2
    if n <= 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1

    a, b = 0, 1
    for i in range(2, n):
        a, b = b, a + b     # a becomes old b
    return b            # b becomes the sum

n = int(input("Enter Number: "))
print(f"The {n}th Fibonacci number is: {fibonacciIterative(n)}")