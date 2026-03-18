import timeit

# RECURSIVELY CALCULATING FIBONACCI SEQUENCE (more difficult example)
# f(n) = f(n - 1) + f(n - 2)
def fibonacci(n):
    if n <= 0:
        return 0 # Base case
    elif n == 1:
        return 1 # Base case 
    else:
        return fibonacci(n - 1) + fibonacci(n - 2) # Recursive case
    
## ITERATIVE CONVERSION: FIBONNACI
def iter_fibonnaci(n):

    if n <= 0:
        return 0
    elif n == 1:
        return 1
    
    a = 0
    b = 1
    
    for i in range(2, n+1):
        c = a+b
        a = b
        b = c

    return b

time1 = timeit.timeit("fibonacci", globals=globals(), number=10000)
time2 = timeit.timeit("iter_fibonnaci", globals=globals(), number=10000)

print("fibonacci:", time1)
print("iter_fibonnaci:", time2)