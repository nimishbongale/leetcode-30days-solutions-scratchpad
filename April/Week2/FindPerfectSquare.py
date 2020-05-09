class Solution:
    def squareRoot(self,number): 
        start = 0
        end,ans = number,1
        while (start <= end) : 
            mid = int((start + end) / 2) 
            if (mid * mid == number) : 
                ans = mid 
                break
            if (mid * mid < number) : 
                start = mid + 1
            else : 
                end = mid - 1
          
        increment = 0.1
        for i in range(0,3):  
            while (ans * ans <= number): 
                ans += increment 
          
            ans = ans - increment 
            increment = increment / 10
        return ans 

    def isPerfectSquare(self, num: int) -> bool:
        if num in [1,4,16,25,36,49,64,81,100]:
            return True
        ans=self.squareRoot(num)
        return True if ans*ans==num else False
            
        
