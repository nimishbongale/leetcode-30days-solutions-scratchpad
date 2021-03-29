class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        stor,sum1,max1={},0,0
        for i in range(len(nums)):
            sum1+=1 if nums[i]==1 else -1
            if sum1==0:
                max1=i+1
            elif sum1 not in stor.keys():
                stor[sum1]=i
            else:
                max1=max(i-stor[sum1],max1)
        return max1
