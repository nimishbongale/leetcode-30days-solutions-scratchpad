class Solution:
    def countBits(self, num: int) -> List[int]:
        ans=[]
        for i in range(num+1):
            ans.append(bin(i).count('1'))
        return ans
