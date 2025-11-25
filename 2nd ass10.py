def karatsuba(x, y):
    if x < 10 or y < 10:
        return x * y
    n = max(len(str(abs(x))), len(str(abs(y))))
    m = n // 2
    pow10 = 10 ** m
    x_high = x // pow10
    x_low  = x %  pow10
    y_high = y // pow10
    y_low  = y %  pow10
    z0 = karatsuba(x_low, y_low)
    z2 = karatsuba(x_high, y_high)
    z1 = karatsuba(x_high + x_low, y_high + y_low) - z2 - z0
    return z2 * (10 ** (2*m)) + z1 * (10 ** m) + z0

# Example:
a = 12345678901234567890
b = 98765432109876543210
print("Karatsuba product (sample):", karatsuba(12345, 67890))
print("Check equality with built-in multiplication:", karatsuba(a,b) == a*b)

