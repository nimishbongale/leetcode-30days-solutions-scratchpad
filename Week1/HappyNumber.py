class Solution:
    stor=[]
    def findhappy(self,n,cnt):
        k=sum([int(x)**2 for x in str(n)])
        if n in self.stor or k in self.stor:
            return True
        if k==1:
            self.stor.append(n)
            return True
        elif cnt>20:
            return False
        return self.findhappy(k,cnt+1)
        
            
    def isHappy(self, n: int) -> bool:
        return self.findhappy(n,0)
