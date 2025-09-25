class Solution:
    def firstMissingPositive(self, nums):
        n = len(nums)
        i = 0
        while i < n:
            correct = nums[i] - 1
            if 0 < nums[i] <= n and nums[i] != nums[correct]:
                nums[i], nums[correct] = nums[correct], nums[i]
            else:
                i += 1
        
        # find first missing positive
        for index in range(n):
            if nums[index] != index + 1:
                return index + 1
        
        return n + 1
