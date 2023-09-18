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
    