import timeit

def factorial(n):
    if n == 0:
        return 1  
    else:
        return n * factorial(n - 1)

def iter_factorial(n):
    
    if_total = 1

    for i in range(1, n+1):

        if_total *= i

    return if_total

time1 = timeit.timeit("factorial", globals=globals(), number=10000)
time2 = timeit.timeit("iter_factorial", globals=globals(), number=10000)

print("factorial:", time1)
print("iter_factorial:", time2)