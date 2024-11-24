class Solution:
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        
        i = 1  
        for j in range(1, len(nums)):
            if nums[j] != nums[j - 1]:  
                nums[i] = nums[j]
                i += 1
        
        return i

nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
solution = Solution()
k = solution.removeDuplicates(nums)
print(k)  
print(nums[:k])  
