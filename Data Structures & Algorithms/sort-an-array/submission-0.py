class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        l = len(nums)

        if l <= 1:
            return nums

        mid = l // 2
        left = nums[:mid]
        right = nums[mid:]

        left = self.sortArray(left)
        right = self.sortArray(right)

        merged = []
        i = 0
        j = 0

        # Compare elements from both sorted lists
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1

        # Add remaining elements
        merged.extend(left[i:])
        merged.extend(right[j:])

        return merged

        