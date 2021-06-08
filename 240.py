# Search a 2D Matrix II
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        
        for i in range(n):
            for j in range(m):
                if matrix[j][i] == target:
                    return True
                elif matrix[j][i] > target:
                    break
        return False