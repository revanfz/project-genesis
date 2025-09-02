def add_binary(a, b):
    # First Solution
    remainder = 0
    sum = str(int(a) + int(b))
    res = ""
    for i in sum[::-1]:
        digit =  int(i) + remainder
        if digit > 1:	
            remainder = int(digit // 2)
        else:
            remainder = 0
        res += f"{digit % 2}"
    
    if remainder:
        res += f"{remainder}"
    
    return res[::-1]
    
    # Solusi kedua, ternyata lebih cepat yang pertama
    # res = ""
    # remainder = 0
    # sum = int(a) + int(b)
    # while sum != 0:
    #     digit = sum % 10 + remainder
    #     sum = int((sum - sum % 10) / 10)
    #     if digit > 1:
    #         remainder = int(digit // 2)
    #     else:
    #         remainder = 0
    #     res += str(digit % 2)

    # if remainder or not res:
    #     res += str(remainder)
        
    # return res[::-1]

print(add_binary("11", "1"))