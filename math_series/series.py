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
    z = [2, 1]
    if n == 0 :
        return z[0]
    elif n == 1:
        return z[1]
    else:
        for r in range(2, n+1):
            a = z[0] + z[1]
            z.append(a)
            z[0] = z[1]
            z[1] = a
            return z[n]

