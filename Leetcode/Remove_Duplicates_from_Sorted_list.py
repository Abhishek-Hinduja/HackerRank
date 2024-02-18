class Solution:
    def removeDuplicates(self, nums):
        if len(nums) < 2:
            return nums

        i = 0
        for item in nums:
            if i < 2 or item != nums[i - 2]:
                nums[i] = item
                i += 1

        ans = i, [int(x) for x in nums[:i]]
        print(*ans)

nums = [1, 1, 1, 2, 2, 3]
S = Solution()
S.removeDuplicates(nums)

