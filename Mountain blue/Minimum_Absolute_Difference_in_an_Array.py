def minimumAbsoluteDifference(arr):
    ans = max(arr)
    for i in range(len(arr)-1):
            ans = min(ans,abs(arr[i]-arr[i+1]))
    print(ans)


arr = [1, -3, 71, 68, 17]
minimumAbsoluteDifference(arr)