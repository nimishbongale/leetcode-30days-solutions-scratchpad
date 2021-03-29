class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        dist={}
        for i in points:
            dist[tuple(i)]=sqrt(i[0]**2+i[1]**2)
        k=sorted(dist,key=lambda x:dist[x])
        return k[:K]
