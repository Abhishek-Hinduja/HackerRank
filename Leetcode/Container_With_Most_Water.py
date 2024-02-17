class Solution:
    def maxArea(self, height):
        Maximum_Water = 0
        left = 0
        right = len(height)-1
        while left<right:
            width = right-left
            h = min(height[left], height[right])
            value = width*h

            if value > Maximum_Water:
                Maximum_Water = value
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return Maximum_Water


height = [1,8,6,2,5,4,8,3,7]
S = Solution()
print(S.maxArea(height))




