class Solution:
    col,newc,arr,m,n,visited=0,0,[],0,0,[]
    def dfs(self,sr,sc):
        if self.arr[sr][sc]==self.col:
            self.arr[sr][sc]=self.newc
        else:
            return
        
        if sr>0 and not self.visited[sr-1][sc]:
            self.visited[sr-1][sc]=True
            self.dfs(sr-1,sc)
        if sc>0 and not self.visited[sr][sc-1]:
            self.visited[sr][sc-1]=True
            self.dfs(sr,sc-1)
        if sc+1<self.n and not self.visited[sr][sc+1]:
            self.visited[sr][sc+1]=True
            self.dfs(sr,sc+1)
        if sr+1<self.m and not self.visited[sr+1][sc]:
            self.visited[sr+1][sc]=True
            self.dfs(sr+1,sc) 
        
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        self.newc=newColor
        self.col=image[sr][sc]
        self.arr=image
        self.m=len(image)
        self.n=len(image[0])
        self.visited=[[False for i in range(self.n)] for j in range(self.m)]
        self.dfs(sr,sc)
        return self.arr
