#Question no 3136
class Solution:
    def isValid(self, word):

        if len(word) < 3:
            return False

        vowels = set("aeiouAEIOU")
        consonants = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ") - vowels
        has_vowel = False
        has_consonant = False

        for char in word:
            if not (char.isdigit() or char.isalpha()):
                return False

            if char in vowels:
                has_vowel = True

            if char in consonants:
                has_consonant = True

        return has_vowel and has_consonant

solution = Solution()
print(solution.isValid("234Adas"))  
print(solution.isValid("b3"))       
print(solution.isValid("a3$e"))     
