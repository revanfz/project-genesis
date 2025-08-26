def is_palindrome(x):
    if x < 0:
        return False
    
    original = x
    reversed = 0
    while x > 0:
        remainder = x % 10
        reversed = reversed * 10 + remainder
        x //= 10

    return reversed == original

print(is_palindrome(121))