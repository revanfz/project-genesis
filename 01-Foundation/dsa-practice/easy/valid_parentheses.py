def valid_parentheses(s) -> bool:
    """ 
    This is the solution i comeup with, failed in 800+ ish test case
    if len(s) % 2 != 0:
        return False
    
    i = 0
    while i < len(s) - 1:
        compare = ord(s[i]) + (1 if ord(s[i]) <= 0x29 else 2)
        if ord(s[i+1]) == compare :
            i += 1
        else:
            for j in range(i+1, len(s), 2):
                if ord(s[j]) == compare:
                    if not valid_parentheses(s[i+1:j]):
                        return False
                    i = j
                elif j == len(s) - 1:
                    return False
        i += 1
        
    return True """
    stack = []
    bracket_map = {")": "(", "}": "{", "]": "["}
    for bracket in s:
        if bracket in bracket_map.values():
            stack.append(bracket)
        elif bracket in bracket_map.keys():
            if not stack or stack.pop() != bracket_map[bracket]:
                return False
    
    return not stack

    '''
    so the approach is you create a map to store the bracket pairs
    then loop the string input, for every bracket value seen, push the seen bracket to the memory
    if the key bracket seen, check whether stack empty or not, if not the opening bracket is not present so it return False
    if the stack not empty also check in the latest stack item (stack.pop()) wheter it is the pair of that bracket by compare it to bracket_map
    if not it also return False
    if the stack empty that mean the bracket is paired each other, so we return not stack (True)
    '''



print(valid_parentheses("(]"))