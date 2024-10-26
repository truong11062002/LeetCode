# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''

              1
           /  |  \
         /         \
       2            3
    /  |  \      /  |  \
   4       5    6       7
   |       |    |       |   
'''
# [4,2,5,1,6,3,7]

stack = []
result = [4, 2, 5, 1, 6, 3, 7]

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        result = []
        
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            
            root = stack.pop()
            result.append(root.val)
            root = root.right
        return result