# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: List[List[int]]
        """
        result = []
        
        def dfs(node, current_path, current_sum):
            if not node:
                return
            
            # Action: Add current node to path and sum
            current_path.append(node.val)
            current_sum += node.val
            
            # Base Case: If it's a leaf node, check the target sum
            if not node.left and not node.right:
                if current_sum == targetSum:
                    result.append(list(current_path))  # Create a copy of the path
            else:
                # Recursion: Traverse children
                dfs(node.left, current_path, current_sum)
                dfs(node.right, current_path, current_sum)
            
            # Backtrack: Remove current node before returning up the tree
            current_path.pop()

        dfs(root, [], 0)
        return result
