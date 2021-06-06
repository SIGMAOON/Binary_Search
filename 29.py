# Divide Two Integers
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        MAX = 2**31 - 1
        MIN = -1*(2**31)
        result = int(dividend/divisor)
        
        if result > MAX:
            return MAX
        elif result < MIN:
            return MIN
        return result