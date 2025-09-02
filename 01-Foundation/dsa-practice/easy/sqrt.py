def sqrt(x):
    # Solusi saya make pendekatan Newton-Raphson
    xn = x // 2
    while True:
        res = 0.5 * (xn + x / xn)
        if abs(xn - res) < 0.000001:
            break
        xn = res
    return int(xn)

print(sqrt(2147395599))    