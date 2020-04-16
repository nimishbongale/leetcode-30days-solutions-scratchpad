class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l,r=[1 for i in range(len(nums))],[1 for i in range(len(nums))]
        for i in range(1,len(nums)):
            l[i]=nums[i-1]*l[i-1]
            r[len(r)-i-1]=nums[len(nums)-i]*r[len(r)-i]
        return [l[i]*r[i] for i in range(len(nums))]
            
        
