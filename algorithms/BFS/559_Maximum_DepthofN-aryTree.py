"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root: return 0
        
        q = deque([root])
        level = 0
        
        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node.children:
                    for child in node.children:
                        q.append(child)
            level += 1
        return level