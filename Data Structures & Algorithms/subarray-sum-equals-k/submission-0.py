class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        current_sum = 0
        answer = 0
        prefix_count = {0: 1}

        for i in nums:
            current_sum += i
            needed_sum = current_sum - k

            if needed_sum in prefix_count:
                answer += prefix_count[needed_sum]

            prefix_count[current_sum] = prefix_count.get(current_sum, 0) + 1

        return answer