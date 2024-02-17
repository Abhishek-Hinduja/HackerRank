# class Solution:
#     def twoSum(self, nums, target):
#         for i in range(len(nums)-1):
#             for j in range(i,len(nums)-1):
#                 if (nums[i]+nums[j]==target):
#                     return i,j

        
# nums = [2,7,11,15]
# target = 9

# S = Solution()
# print(S.twoSum(nums,target))

class Solution:
    def twoSum(self, nums, target):
        dic = {}
        for i in range(len(nums)):
            value = target-nums[i]
            if value in dic:
                return dic[value],i
            dic[nums[i]] = i
        return dic
    

nums = [2,7,11,15]
target = 9

S = Solution()
print(S.twoSum(nums,target))

