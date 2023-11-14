## Find a Contiguous Subarray Which has the largest Sum in the 1-d array *imp

def contiguous_arr(array):
    j = 0
    k = 0
    sum = 0
    maximum_sum = -64684768
    for i in range(len(array)):
        sum += array[i]
        if sum < 0:
            sum = 0 
            j = i+1
        if sum > maximum_sum:
            maximum_sum = sum
            k = i

    for i in range(j,k+1):
        print(array[i], end = ' ')

array = [2,7,3,4,5,2]
contiguous_arr(array)