class Solution:
    def myAtoi(self, s:str) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        res = 0
        isNegative = False
        isPositive = False
        meetDigit = False

        for char in s:
            if meetDigit == False and char == '-':
                isNegative = True
            elif meetDigit == False and char == '+':
                isPositive = True

            elif '0' <= char <= '9':
                meetDigit = True
                res = res*10 + ord(char) - ord('0') 
                if res > INT_MAX:
                    return INT_MIN if isNegative else INT_MAX
            
            elif char != ' ':
                if isNegative:
                    return -res
                elif not isNegative:
                    return res
                else: 
                    return 0

        if isNegative:
            return -res
        elif isNegative and isPositive:
            return 0
        else: 
            return res
            
example = Solution()
print(example.myAtoi('1337c0d3'))