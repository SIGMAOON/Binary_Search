# Kth Smallest Element in a Sorted Matrix
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        _all = []
        for num in matrix:
            for n in num:
                _all.append(n)
        _all.sort()
        return _all[k-1]