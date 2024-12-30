# Question no 58
class Solution:
    def lengthOfLastWord(self, s):

        words = s.strip().split()
        return len(words[-1])

solution = Solution()
s1 = "Hello World"
s2 = "   fly me   to   the moon  "
s3 = "luffy is still joyboy"

print(solution.lengthOfLastWord(s1))  
print(solution.lengthOfLastWord(s2))  
print(solution.lengthOfLastWord(s3))  
