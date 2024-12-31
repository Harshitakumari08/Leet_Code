# Question no 136
class Solution:
    def singleNumber(self, nums):
        result = 0
        for num in nums:
            result ^= num 
        return result

solution = Solution()
nums1 = [2, 2, 1]
nums2 = [4, 1, 2, 1, 2]
nums3 = [1]

print(solution.singleNumber(nums1))  
print(solution.singleNumber(nums2))  
print(solution.singleNumber(nums3))  
