# Find the Duplicate Number
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        dic = {}
        for num in nums:
            dic[num] = 0
        for num in nums:
            dic[num]+=1
            if dic[num] > 1:
                return num