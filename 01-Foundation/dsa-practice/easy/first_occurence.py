# So basically this function return where does the beginning of the needle founded, which index
# I'm quite happy with my solution gets 0ms runtime, lezgoww
def first_occurence(haystack, needle):
    target = len(needle)
    for i in range(len(haystack) - target + 1):
        if haystack[i:i+target] == needle:
            return i
        
    return -1

print(first_occurence("a", "a"))