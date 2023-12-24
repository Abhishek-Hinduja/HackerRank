def viralAdvertising(n):
    cumulative = 0
    val = 5

    for i in range(1,n+1):
        liked = val//2
        cumulative += liked
        val = liked * 3

    return cumulative

print(viralAdvertising(5))
