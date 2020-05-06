# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, x: int, y: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        dim=binaryMatrix.dimensions()
        p={0:0,1:dim[1]-1}
        while p[0]!=dim[0] and p[1]!=-1:
            if binaryMatrix.get(p[0],p[1])==0:
                p[0]=p[0]+1
            else:
                p[1]=p[1]-1
        k=p[1]+1
        return -1 if k==dim[0] else k
                
