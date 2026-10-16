class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        n = len(nums) / 3
        seen = dict()
        ans = []
        for i in nums:
            if seen.get(i) == None:
                seen.update({i:1})
            else:
                x = seen.get(i)
                x = x+1
                seen.update({i:x})
        for i in seen:
            if seen.get(i)>n:
                ans.append(i) 
        return ans