print(256%83)

def fast_power(a, n):

    # basisgeval
    if n == 0:
        return 1

    # even exponent
    if n % 2 == 0:
        half = fast_power(a, n // 2)
        return half * half

    # oneven exponent
    return a * fast_power(a, n - 1)

print(fast_power(2,5))