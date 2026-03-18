import timeit

# BASIC RECURSION EXAMPLE
def sum_of_natural_numbers(n):
    if n == 1:
        return 1 
    else:
        return n + sum_of_natural_numbers(n - 1)
    
## ITERATIVE CONVERSION: SUM
def iter_sum_of_natural_numbers(n):
    total = 0

    for i in range(1, n+1):
        total += i

    return total
    
time1 = timeit.timeit("sum_of_natural_numbers", globals=globals(), number=10000)
time2 = timeit.timeit("iter_sum_of_natural_numbers", globals=globals(), number=10000)

print("sum_of_natural_numbers:", time1)
print("iter_sum_of_natural_numbers:", time2)