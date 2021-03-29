class Solution:
    def doshift(self,s,d,a):
        if d==0:
            return s[a:]+s[:a]
        return s[len(s)-a:]+s[:len(s)-a]
    
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        for i in shift:
            s=self.doshift(s,i[0],i[1])
            print(s)
        return s
