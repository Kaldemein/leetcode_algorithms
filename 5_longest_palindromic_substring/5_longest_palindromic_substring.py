class Solution:
    def longestPalindrome(self, s: str) -> str:
        lngst_pal = ''
        cur_pal = ''

        for i in range(len(s)):
            #odd
                left, right = i, i
                while left >= 0 and right < len(s) and s[left] == s[right]:
                    cur_pal = s[left:right+1]
                    if len(lngst_pal) < len(cur_pal):
                        lngst_pal = cur_pal
                    left = left-1
                    right = right+1
            #even
                left, right = i, i+1
                while left >= 0 and right < len(s) and s[left] == s[right]:
                    cur_pal = s[left:right+1]
                    if len(lngst_pal) < len(cur_pal):
                        lngst_pal = cur_pal
                    left = left-1
                    right = right+1
        if len(lngst_pal)==0:
            lngst_pal = s[0]
        return lngst_pal

s = 'babaddabab'

example = Solution()

print(example.longestPalindrome(s))
                 
