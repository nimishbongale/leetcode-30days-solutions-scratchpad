class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        if len(trust)==0:
            return 1
        mydic,npos,pos={},[],[]
        for i in trust:
            mydic[i[1]]=mydic.get(i[1],[])
            mydic[i[1]].append(i[0])
            npos.append(i[0])
            pos.append(i[1])

        for i in set(pos):
            if i not in npos and len(mydic[i])==N-1:
                return i
        return -1
            
            
        
