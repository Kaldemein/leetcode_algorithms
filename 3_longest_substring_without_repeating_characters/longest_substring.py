# s = 'c'

# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
        

#         dict = {}
#         max_length = 0 
#         current_string_length = 0

#         for char in s:
#             if char not in dict:
#                 dict[char] = None
#                 current_string_length +=1
#                 if max_length < current_string_length:
#                     max_length = current_string_length
#             else: 
#                 if max_length < current_string_length:
#                     max_length = current_string_length
#                 dict.clear()
#                 dict[char] = None
#                 current_string_length = 1
        
#         return max_length 
    
# example = Solution()

# print(example.lengthOfLongestSubstring(s))



class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        def compareLength(max_length, current_substr):
            if max_length < len(current_substr):
                max_length = len(current_substr)
            return max_length

        max_length = 0
        current_substr = []

        for char in s:
            if char not in current_substr:
                current_substr.append(char)
                max_length = compareLength(max_length, current_substr)
            else: 
                del current_substr[0:current_substr.index(char)+1]
                current_substr.append(char)
                max_length = compareLength(max_length, current_substr)
        return max_length

    
example = Solution()

print(example.lengthOfLongestSubstring('ohvhjdml'))