def karatsuba(a,b):
    if a < 10 or b < 10:
        return a*b
    
    lengte = max(len(str(a)), len(str(b)))
    halve_lengte = lengte // 2


    #h1 = int(str(a)[:halve_lengte])
    #h2 = int(str(a)[:halve_lengte])
    a_h = a // 10**halve_lengte
    a_l = a % 10**halve_lengte
    b_h = b // 10**halve_lengte
    b_l = b % 10**halve_lengte

    z0 = karatsuba(a_l,b_l)
    z1 = karatsuba(a_h,b_h)
    z2 = karatsuba((a_h+a_l),(b_h+b_l))

    return (z1 * 10**(halve_lengte*2)) + ((z2-z1-z0) * 10**halve_lengte) + z0



print(karatsuba(123456,9876543210))
print(123456*9876543210)