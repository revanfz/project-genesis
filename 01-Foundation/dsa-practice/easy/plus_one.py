def plusOne(digits: list[int]):
    # list_to_num = int("".join([str(a) for a in digits])) + 1
    # new_digits = []
    # while list_to_num > 0:
    #     digit = list_to_num % 10
    #     new_digits.append(digit)
    #     list_to_num = int((list_to_num - digit) / 10)
    
    # return new_digits[::-1]


    # check from behind, if not 9 stop, if it is how much it appears consecutively
    # by default we need to change 1 digit, so we ignore the furthest digit
    # that's because  we keep increasing digit_change as the loop not break
    # because if it happen to be number 9 for n consecutive time it will represented correctly instead of n+1
    digit_change = 1
    for digit in digits[:-1][::-1]:
        if digit != 9:
            break
        digit_change += 1

    # after finding how many digit we need to change, we change the first of that digit to be
    # the first digit = remainder of its (value + 1) module by 10
    remainder = (digits[-digit_change] + 1) % 10
    # if the remainder exist, whe change its value to remainder, else we change it to 1
    # and we need to repeat 0 for digit_change - 1 times
    digits[-digit_change] = remainder if remainder else 1
    if not remainder:
        digits[len(digits)-digit_change+1:] = [0] * digit_change

    return digits

print(plusOne([8, 9, 9, 9]))