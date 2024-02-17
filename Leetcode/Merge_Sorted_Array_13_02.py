# class Solution:
#     def merge(self, nums1, m, nums2, n):
#         nums3 = []
#         i = 0
#         while i < m:
#             nums3.append(nums1[i])
#             i+=1
#         j,k,l = 0,0,0
#         while j < m and k < n:
#             if nums3[j] < nums2[k]:
#                 nums1[l] = nums3[j] 
#                 l += 1
#                 j += 1
#             elif nums3[j] > nums2[k]:
#                 nums1[l] = nums2[k]
#                 l += 1
#                 k += 1
#             else:
#                 nums1[l] = nums3[j]
#                 l += 1
#                 j += 1
#         while j < m:
#             nums1[l] = nums3[j]
#             l += 1
#             j += 1
#         while k < n:
#             nums1[l] = nums2[k]
#             l += 1
#             k += 1
#         return nums1


# nums1 = [1,2,3,0,0,0]
# m = 3
# nums2 = [2,5,6]
# n = 3

# S = Solution()
# print(S.merge(nums1, m, nums2, n))


# class Solution:
#     def merge(self, nums1, m, nums2, n):
#         i, j, k = m - 1, n - 1, m + n - 1
        
#         while i >= 0 and j >= 0:
#             if nums1[i] > nums2[j]:
#                 nums1[k] = nums1[i]
#                 i -= 1
#             else:
#                 nums1[k] = nums2[j]
#                 j -= 1
#             k -= 1

#         while j >= 0:
#             nums1[k] = nums2[j]
#             j -= 1
#             k -= 1

#         return nums1

# nums1 = [1, 2, 3, 0, 0, 0]
# m = 3
# nums2 = [2, 5, 6]
# n = 3

# S = Solution()
# print(S.merge(nums1, m, nums2, n))
