# def reverse_an_array(arr):
#     hp = 0
#     lp = len(arr)-1
#     while hp<=lp:
#         temp = arr[hp]
#         arr[hp] = arr[lp]
#         arr[lp] = temp
#         hp+=1
#         lp-=1
#     return arr

# arr = [1,2,3,4,5]
# print(reverse_an_array)

# def max_min(arr):
#     maximum = arr[0]
#     minimum = arr[0]
#     for i in range(len(arr)):
#         if arr[i] > maximum:
#             maximum = arr[i]
#         if arr[i] < minimum:
#             minimum = arr[i]

#     return maximum,minimum

# arr = [1,2,3,4,5]
# print(max_min(arr))


# def additiion_Swap(a,b):
#     a = a + b
#     b = a - b
#     a = a - b
#     print(a,b)
    
# additiion_Swap(50,20)

# def multiplication_divison(a,b):
#     a = a * b
#     b = a // b
#     a = a // b
#     print(a,b)

# multiplication_divison(50,20)


# def kth_maxim_minimun(arr,k):
#     arr.sort()
#     maximum = arr[len(arr)-k]
#     minimum = arr[k-1]
#     return maximum, minimum

# arr = [1,2,52,4,5,9,6]
# print(kth_maxim_minimun(arr,2))
    
# Sort the array with 0's and 1's and 2's without using any sorting algorithm

# def sort_0s_1s_2s(arr):
#     low = 0
#     mid = 0
#     high = len(arr) - 1

#     while (mid<=high):
#         if arr[mid] == 0:
#             arr[mid],arr[low] = arr[low], arr[mid]
#             mid += 1
#             low += 1
#         elif arr[mid] == 1:
#             mid += 1
#         elif arr[mid] == 2:
#             arr[mid], arr[high] = arr[high], arr[mid]
#             high  -= 1

#     return arr

# arr = [0,1,0,2,0,1,0,1,2,0,1,2]
# print(sort_0s_1s_2s(arr))

# def sort_negative_positive(arr):
#     low = 0
#     high = len(arr)-1

#     while low<=high:
#         if arr[low] < 0:
#             low += 1
#         elif arr[high] > 0:
#             high -= 1
#         else:
#             arr[low], arr[high] = arr[high], arr[low]
#             low += 1
#             high -= 1
#     low += 1
#     high -= 1
#     return arr

# arr = [1,0,5,-8,9,-6,8,9,2,-5]
# print(sort_negative_positive(arr))

# def union_intersection(arr1,arr2):
#     i,j = 0, 0
#     union = set()
#     intersection = []
#     while i < len(arr1) and j < len(arr2):
#         if arr1[i] > arr2[j]:
#             union.add(arr1[i])
#             i += 1
#         elif arr1[i] < arr2[j]:
#             union.add(arr2[j])
#             j += 1
#         elif arr1[i] == arr2[j]:
#             union.add(arr1[i])
#             i += 1
#             j += 1

#     while i < len(arr1):
#         union.add(arr1[i])
#         i += 1
#     while j < len(arr2):
#         union.add(arr2[j])
#         j += 1 

#     for i in range(len(arr2)):
#         for j in range(len(arr1)):
#             if arr2[i] == arr1[j]:
#                 intersection.append(arr2[i])
#     return union,intersection


# arr1 = [1,2,3,4,5]
# arr2 = [3,4]
# print(union_intersection(arr1,arr2))


### Maximum sum of subarray using kaden's algorithm


# def max_sum(arr):
#     sum = 0
#     max_sum =  -(10**10)

#     for i in range(len(arr)):
#         sum += arr[i]
#         if sum<0:
#             sum = 0
#         if sum > max_sum:
#             max_sum = sum
#     return max_sum

# arr =  [5,4,-8,6,-8,1,-8,9,6,2,-8,5,8,-11]
# print(max_sum(arr))

## time conversion 12hour to 24hour
# def timeConversion(time):
#     # Write your code here
#     a = time[-2::]
#     out = ''
    
#     if a=="PM" and int(time[0:2]) != 12:
#         b = int(time[0:2])
#         c = 12 + b
#         out = str(c) + time[2:8]
#     elif a == "PM" and int(time[0:2]) == 12:
#         out = time[0:8]
        
#     if a == "AM" and int(time[0:2]) == 12:
#         b = int(time[0:2])
#         c = b - 12
#         out = '0' + str(c) + time[2:8] 
#     elif a == "AM" and 1 <= int(time[0:2]) <= 11:
#         out = time[0:8]
#     return out
        

# find duplicates in n + 1 Array

# def duplicates(arr):
#     for i in range(len(arr)):
#         num = abs(arr[i])
#         if arr[num] >= 0:
#             arr[num] = -arr[num]
#         else:
#             print(num)
# arr = [1,2,3,3,4]
# duplicates(arr)