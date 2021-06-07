# Median of Two Sorted Arrays
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total = nums1 + nums2
        total.sort()
        l = len(total)
        if l % 2 == 1:
            return total[l//2]
        return (total[l//2] + total[l//2 - 1])/2