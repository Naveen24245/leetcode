class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()
        closest_sum = float('inf')
        n = len(nums)

        for i in range(n):
            left, right = i + 1, n - 1

            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]

                # Update closest_sum if this one is closer to target
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum

                # Move pointers based on comparison
                if current_sum < target:
                    left += 1
                elif current_sum > target:
                    right -= 1
                else:
                    # Found exact match
                    return current_sum

        return closest_sum
sol = Solution()

print(sol.threeSumClosest([-1, 2, 1, -4], 1))


print(sol.threeSumClosest([0, 0, 0], 1))

