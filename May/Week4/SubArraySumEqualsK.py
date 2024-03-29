class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sums = defaultdict(int)
        current_sum = 0
        num_subarrays = 0
        sums[0] = 1
        for v in nums:
            current_sum += v
            num_subarrays += sums[current_sum - k]
            sums[current_sum] += 1
        return num_subarrays
