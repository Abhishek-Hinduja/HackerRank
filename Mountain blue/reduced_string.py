# Reduce a string of lowercase characters in range ascii[‘a’..’z’]by doing a series of operations. In each operation, select a pair of adjacent letters that match, and delete them.
# Delete as many characters as possible using this method and return the resulting string. If the final string is empty, return Empty String.

def superReducedString(s):
    empty_stack = []

    for i in range(len(s)):
        if empty_stack and s[i] == empty_stack[-1]:
            empty_stack.pop()
        else:
            empty_stack.append(s[i])
    if empty_stack:
        return "".join(empty_stack)
    else:
        return "Empty String"
        
    

s = "baab"
print(superReducedString(s))