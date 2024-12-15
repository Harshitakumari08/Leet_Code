import re

class Solution:
    def isPalindrome(self, s):
        cleaned = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        return cleaned == cleaned[::-1]

solution = Solution()

print(solution.isPalindrome("A man, a plan, a canal: Panama"))  
print(solution.isPalindrome("race a car"))                     
print(solution.isPalindrome(" "))                              
