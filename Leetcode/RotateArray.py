class Solution:
    def rotate(self, nums, k):
        n = k%len(nums)

        def reverse(array, start, end):
            while start<end:
                array[start], array[end] = array[end], array[start]
                start+=1
                end-=1

        reverse(nums, 0,len(nums)-1)

        reverse(nums,0,n-1)

        reverse(nums,n,len(nums)-1)

        return nums


S = Solution()
nums = [1,2,3,4,5,6,7]
k = 3
S.rotate(nums,k)