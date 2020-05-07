# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        nodes = [] # (depth, parent)
        
        def dfs(node: TreeNode, parent: TreeNode, depth: int):
            
            if not node or len(nodes) == 2: # no. of nodes won't be less than 2
                return
            else:
                if node.val == x or node.val == y:
                    nodes.append((depth, parent))
                dfs(node.left, node, depth + 1)
                dfs(node.right, node, depth + 1)
        
        dfs(root, None, 0)
        
         # col 0: depth, col2: parent therefore, nodes[0][0]==nodes[1][0] and nodes[0][1] != nodes[1][1]
         # the column 1 vals(depth) should be equal but the col2 vals (x, y) mustn't be equal since they're unique
        if(nodes[0][0] == nodes[1][0] and nodes[0][1] != nodes[1][1]):
            return True
        else:
            return False