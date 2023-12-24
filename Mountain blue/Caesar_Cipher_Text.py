def caesarCipher(s, k):
    ans = ""
    for i in s:
        if i.isalpha(): 
            if i.islower():
                ans += chr((ord(i) - ord('a') + k) % 26 + ord('a'))
            elif i.isupper():
                ans += chr((ord(i) - ord('A') + k) % 26 + ord('A'))
        else:
            ans += i
    print(ans)
s = "middle-Outz"
k = 2
caesarCipher(s,k)