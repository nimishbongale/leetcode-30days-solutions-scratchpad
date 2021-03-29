class Solution:
    def frequencySort(self, s: str) -> str:
        d=Counter(s)
        ans=''
        k=sorted(d,key=lambda x:d[x],reverse=True)
        for i in k:
            ans+=i*d[i]
        return ans
