class Solution:
    def getConcatenation(self, nums):
        ans = [0]*(2*len(nums))

        for i in range(len(nums)):
            ans[i] = nums[i]
            ans[i+len(nums)] = nums[i]

        return ans


nums = [1,2,1]
S = Solution()
print(S.getConcatenation(nums))