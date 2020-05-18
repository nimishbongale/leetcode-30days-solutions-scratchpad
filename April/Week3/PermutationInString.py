class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #s1 is p, s2 is s
        n = len(s2)
        m = len(s1)
        s1 = Counter(s1)
        ans = []
        for i in range(0,n-m+1):
            if i == 0: 
                window = Counter(s2[:m])   
            else:    
                window[s2[i-1]] -= 1       
                window[s2[i+m-1]] += 1     
            if len(window - s1) == 0:      
                return True
        return False
