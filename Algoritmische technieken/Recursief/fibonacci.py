def fibonacci(n,step):
    print(f"{" "*step}Fibonacci {n}")
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n-1,step+1)+fibonacci(n-2,step+1)

print(fibonacci(10,0))
