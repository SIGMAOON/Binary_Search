# Find First and Last Position of Element in Sorted Array
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        answer = []
        for i in range(len(nums)):
            if nums[i] == target:
                answer.append(i)
                
        if answer == []:
            return [-1,-1]
        return [answer[0],answer[-1]]