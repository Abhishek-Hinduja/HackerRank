# Given an array of bird sightings where every element represents a bird type id, determine the id of the most frequently sighted type. If more than 1 type has been spotted that maximum amount, return the smallest of their ids.

def migratoryBirds(arr):
    dic = {}

    for item in arr:
        if item not in dic:
            dic[item] = 1
        else:
            dic[item] += 1
    
    ans = max(arr)
    maxfreq = max(dic.values())

    for item in dic:
        if dic[item]==maxfreq:
            ans = min(ans,item)

    return ans

arr = [1,4,4,4,5,3]
print(migratoryBirds(arr))