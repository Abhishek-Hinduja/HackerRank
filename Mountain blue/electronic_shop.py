def getMoneySpent(keyboards, drives, b):
    sum = -1
    for i in range(len(keyboards)-1):
        for j in range(len(drives)-1):
            if (keyboards[i] + drives[j]) < b and (keyboards[i] + drives[j]) > sum:
                sum = (keyboards[i] + drives[j])
    print(sum)


b = 5
Keyboards = [4]
drives = [5]

getMoneySpent(Keyboards, drives, b)