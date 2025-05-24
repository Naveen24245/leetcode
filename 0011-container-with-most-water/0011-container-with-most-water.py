class Solution:
    def maxArea(self, height):
        left, right = 0, len(height) - 1
        max_area = 0

        while left < right:
            h = min(height[left], height[right])
            width = right - left
            area = h * width
            max_area = max(max_area, area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area

# Example usage
s = Solution()
print(s.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))  # Output: 49
