#Intersection of Two Arrays II
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        # 76ms, 14.3 MB
        
        intersection = []
        
        for num in nums1:
            if num in nums2:
                intersection.append(num)
                nums2.remove(num)
        return sorted(intersection)
