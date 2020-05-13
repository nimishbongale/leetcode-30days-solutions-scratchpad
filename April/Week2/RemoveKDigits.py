class Solution:
    def removeKdigits(self, num: str, k: int) -> str:    
        ans=''
        for i in num:
            while k>0 and len(ans)>0 and ans[-1]>i:
                k-=1
                ans=ans[:-1]  
            ans+=i
        if k>0:
            ans=ans[:-k]     
        return str(int(ans)) if len(ans)!=0 else '0'
