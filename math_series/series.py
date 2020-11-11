def fibonacci(n): # recursion 
    if n < 0:
        print('error')
    elif n <= 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    else:
       return (fibonacci(n-1)+ fibonacci(n-2))

print(fibonacci(1))

def lucas(n):
    if n == 0:
        return 2
    elif n == 1:
        return 1
    elif n == 2:
        return 3
    else:
        return (lucas(n-1) + lucas(n-2))

print(lucas(1))

def sum_series(n, x=0, y=1):
    if n == 0:
        return x
    elif n == 1:
        return y
    else:
        return (sum-series(n-1, x, y) + sum_series(n-2, x, y))

print(sum_series(0, 2, 1))
