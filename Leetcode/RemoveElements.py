class Solution:
    def removeElement(self, nums, val):

    
        i = 0
        while i < len(nums):
            if nums[i] == val:
                nums.pop(i)
            else:
                i+=1
        return len(nums)

S = Solution()
nums = [3,2,2,3]
val = 2
print(S.removeElement(nums,val))