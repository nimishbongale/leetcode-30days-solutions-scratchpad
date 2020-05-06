class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if len(matrix)<1:
            return 0
        dp=[[0 for i in range(len(matrix[0])+1)] for j in range(len(matrix)+1)]
        max1=0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]=='1':
                    dp[i+1][j+1]=min(dp[i][j],dp[i][j+1],dp[i+1][j])+1
                    max1=max(max1,dp[i+1][j+1])
        return max1**2
        
        
        
        
        
        
