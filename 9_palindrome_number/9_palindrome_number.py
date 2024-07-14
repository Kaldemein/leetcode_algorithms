class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        i = len(s) // 2

        if len(s) % 2 == 0:
            left, right = i-1, i
            print(left, right)
            while left >= 0 and right < len(s):
                if s[left] == s[right]:
                    left -=1
                    right+=1
                else: 
                    return False
            return True
        else: 
            left, right = i, i
            while left >=0 and right < len(s):
                if s[left]==s[right]:
                    left -=1
                    right+=1
                else:
                    return False
            return True
        
example = Solution()
print(example.isPalindrome(10))
