def minimumNumber(n, password):
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"
    number, lower_cas, upper_cas, special_character = False, False, False, False
    ans = 0

    for i in range(len(password)):
        if password[i] in numbers:
            number = True
        elif password[i] in lower_case:
            lower_cas = True
        elif password[i] in upper_case:
            upper_cas = True
        elif password[i] in special_characters:
            special_character = True
    if not number:
        ans += 1
    if not lower_cas:
        ans += 1
    if not upper_cas:
        ans += 1
    if not special_character:
        ans += 1
    if n >= 6:
        return ans
    else:
        return max(ans,6 - n)

print(minimumNumber(3,"Ab1"))

    
    
