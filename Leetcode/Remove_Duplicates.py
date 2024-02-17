class Solution:
    def removeDuplicates(self, nums):
        k = 1
        for i in range(1,len(nums)-1):
            if nums[i] != nums[i-1]:
                nums[k] = nums[i]
                k += 1
        return k




nums = [0,0,1,1,1,2,2,3,3,4]
S = Solution()
result = S.removeDuplicates(nums)
print(result)