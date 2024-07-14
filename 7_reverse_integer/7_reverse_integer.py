class Solution:
    def reverse(self, x: int) -> int:
        digits = []
        total = 0 
    
        abs_x = abs(x)

        while abs_x > 0: 
            digit = abs_x % 10
            abs_x = abs_x // 10
            total = total*10 + digit

        if total < -2**31 or total > 2**31 - 1:
            return 0

        if x > 0:
            return total
        else:
            return -total        
        return total


example = Solution()

print(example.reverse(1534236469))