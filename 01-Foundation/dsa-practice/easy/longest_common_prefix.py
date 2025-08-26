def lcp(strs: list[str]):
    reference = strs[0]
    if not reference:
        return ""
    for i in range(len(reference)):
        currentChar = reference[i]
        for j in range(1, len(strs)):
            if i > len(strs[j]) or currentChar != strs[j][i] or not(strs[j]):
                return reference[:i]
    return reference
                
print(lcp(["flower", "flower", "flower", "flower"]))