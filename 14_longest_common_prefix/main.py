from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prev_pref = strs[0]
        
        for i in range(1, len(strs)):
          word = strs[i]
          
          j = 0
          while j < len(prev_pref) and j < len(word) and prev_pref[j] == word[j]:
            j += 1
          prev_pref = prev_pref[:j]
        if prev_pref:
          return prev_pref
        else:
          return ""
              
          
example = Solution()
print(example.longestCommonPrefix(["dog","racecar","car"]))