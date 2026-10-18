class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        temp = nums1[:m]
        p1 =0
        p2 = 0
        for i in range(len(nums1)): 
            if p1 < m and p2 < n:
                if temp[p1]<nums2[p2]:
                    print(temp[p1],"-----")
                    nums1[i]=temp[p1]
                    p1 +=1
                else:
                    print(nums2[p2],"_____")
                    nums1[i]=nums2[p2]
                    p2+=1
            else:
                if p1 >= m:
                    nums1[i]=nums2[p2]
                    p2+=1
                else:
                    nums1[i]=temp[p1]
                    p1 +=1
        return nums1