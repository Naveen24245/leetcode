class Solution:
    def sortColors(self, nums):
        c0 = c1 = c2 = 0

        # Count 0s, 1s, and 2s
        for num in nums:
            if num == 0:
                c0 += 1
            elif num == 1:
                c1 += 1
            else:
                c2 += 1

        # Overwrite array
        for i in range(len(nums)):
            if i < c0:
                nums[i] = 0
            elif i < c0 + c1:
                nums[i] = 1
            else:
                nums[i] = 2