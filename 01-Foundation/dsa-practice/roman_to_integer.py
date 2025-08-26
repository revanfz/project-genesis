def roman_to_int(s):
    res = 0
    roman_map = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    i = 0
    while i < len(s):
        if roman_map[s[i]] in [1, 10, 100] and i < len(s) - 1 and roman_map[s[i+1]] > roman_map[s[i]]: # here's where i fumbled a bit
            res += roman_map[s[i+1]] - roman_map[s[i]]
            i += 1
        else:
            res += roman_map[s[i]]
        i += 1
    return res

    # best solution
    # for i in range(len(s)):
    #     if i + 1 < len(s) and roman_map[s[i]] < roman_map[s[i+1]]:
    #         res -= roman_map[s[i]]
    #     else:
    #         res += roman_map[s[i]]

print(roman_to_int('MCMXCIV'))