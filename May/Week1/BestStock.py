class Solution:
    def maxProfit(self, p: List[int]) -> int:
        if sorted(p,reverse=True)==p:
            return 0
        elif sorted(p)==p:
            return p[-1]-p[0]
        else:
            lmin,lmax,i,ans=0,0,0,0
            while i<len(p)-1:
                lmin,lmax,nmin,nmax=0,0,True,True
                while i<len(p)-1:
                    if p[i]<=p[i+1]:
                        lmin=p[i]
                        nmin=False
                        i+=1
                        break
                    i+=1
                while i<len(p)-1:
                    if p[i]>=p[i+1]:
                        lmax=p[i]
                        i+=1
                        nmax=False
                        break
                    i+=1
                if nmin and nmax:
                    break
                elif nmax:
                    ans+=p[-1]-lmin
                else:
                    ans+=lmax-lmin
            return ans
