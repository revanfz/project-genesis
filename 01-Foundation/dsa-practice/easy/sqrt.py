def sqrt(x):
    # Solusi saya make pendekatan Newton-Raphson
    xn = x // 2
    while True:
        res = 0.5 * (xn + x / xn)
        if abs(xn - res) < 0.000001:
            break
        xn = res
    return int(xn)

    # Karena problemnya cuma pengen int terdekat kebawah (floored)
    # ini pendekatan yang lebih simpel, tapi ini runtimenya lebih lama sih
    # if x < 1:
    #     return x
    
    # res = 1
    # i = 1
    # while res <= x:
    #     i += 1
    #     res = i * i

    # return i - 1

print(sqrt(4))    