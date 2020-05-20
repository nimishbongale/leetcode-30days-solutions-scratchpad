# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    ans=[]
    def inord(self,root):
        if root!=None:
            self.inord(root.left)
            self.ans.append(root.val)
            self.inord(root.right)
    
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.ans=[]
        self.inord(root)
        return self.ans[k-1]
            
        
        
