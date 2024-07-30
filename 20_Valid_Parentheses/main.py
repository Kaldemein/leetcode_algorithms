class Solution:
    def isValid(self, s: str) -> bool:
        openBracket = []
        
        bracketCouples = {
          ")": "(",
          "}": "{",
          "]": "["
        }
        
        if len(s) == 0 or len(s) == 1:
          return False
        
        for i, value in enumerate(s):
          if value == '(' or value == '{' or value == '[':
            openBracket.append(value)
          else:
            if value == ')' or value == '}' or value == ']':
              if len(openBracket) > 0 and openBracket[-1] == bracketCouples[value]:
                del openBracket[-1]
              else:
                return False
        if len(openBracket) == 0:
          return True
        else:
          return False       
        
example = Solution()
print(example.isValid('()[]'))