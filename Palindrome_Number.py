class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        
        reversed_number = 0
        original = x

        while x > 0:
            digit = x % 10  
            reversed_number = reversed_number * 10 + digit   
            x //= 10  
        
        return original == reversed_number

solution = Solution()
print(solution.isPalindrome(121))   
print(solution.isPalindrome(-121))  
print(solution.isPalindrome(10)) 
