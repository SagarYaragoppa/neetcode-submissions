class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        count = 0
        x = 0
        seen = set()
        for i in nums:
            if i not in seen:
                seen.add(i)
                if nums.count(i)> count:
                    x = i
                    count = nums.count(i)
        return x             