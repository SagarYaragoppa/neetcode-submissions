class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)

        # Step 1: Replace invalid numbers
        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = n + 1

        # Step 2: Mark numbers that exist
        for i in range(n):
            x = abs(nums[i])

            if 1 <= x <= n:
                nums[x - 1] = -abs(nums[x - 1])

        # Step 3: Find the first missing positive
        for i in range(n):
            if nums[i] > 0:
                return i + 1

        return n + 1