# ## Question 1) ##list-comprehensions There are 3 integers given x,y,z we have to return using list comprehension method where sum of i+j+k != n

# x =  int(input())
# y = int(input())
# z = int(input())
# n = int(input())

# ans = [[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k != n]
# print(ans)

# ### Question 2) ##Finding the Secondmaximum from the array

# def secondmax(arr,n):
#     firstmax = -458
#     secondmax = -458

#     for num in arr:
#         if num > firstmax:
#             secondmax = firstmax
#             firstmax = num
#         elif num > secondmax and num != firstmax:
#             secondmax = num
#     print(secondmax)

# if __name__ == "__main__":
#     arr = list(map(int, input().split()))
#     n = len(arr)
#     secondmax(arr,n)

def binarysearch(arr, x, left, right):
    count = 0
    
    while left <= right:  # Change the condition to handle the case when left == right
        mid = (left + right) // 2

        if arr[mid] == x:
            count += 1
            # Check the elements to the right of mid
            i = mid + 1
            while i <= right and arr[i] == x:
                count += 1
                i += 1

            # Check the elements to the left of mid
            i = mid - 1
            while i >= left and arr[i] == x:
                count += 1
                i -= 1

            break  # We have found all occurrences of x, so break out of the loop
        elif arr[mid] > x:
            right = mid - 1
        else:
            left = mid + 1

    return count

arr = [1, 2, 3, 4, 5, 6, 6, 6,6, 8, 9]
print(binarysearch(arr, 6, 0, len(arr) - 1))

