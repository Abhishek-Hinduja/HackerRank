def camelcase(s):

    total = 1

    for i in s:
        if ord(i) >= 65 and ord(i) <= 90:
            total+=1
    print(total)


s = "saveChangesInTheEditor"
camelcase(s)