class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d=Counter(nums)
        n=len(nums)
        for i in d.keys():
            if d[i]> n//2:
                return i
        
