class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        list1 =[]
        l = len(nums)
        prefix = []
        suffix = []
        for i in range(len(nums)):
            if i == 0:
                prefix.append(1)
            else:
                x = prefix[i-1]*nums[i-1]
                prefix.append(x)
        y = 0
        for i in range(l-1,-1,-1):
            
            if i == l-1:
                suffix.append(1)
            else:
                x = suffix[y]*nums[i+1]
                suffix.append(x) 
                y+=1 
        suffix_reversed = suffix[::-1]
        for i in range(len(nums)):
            ans = prefix[i]*suffix_reversed[i]
            list1.append(ans)
        return list1