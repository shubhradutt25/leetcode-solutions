class Solution(object):
    def flatten(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: None Do not return anything, modify root in-place instead.
        """

        current = root

        while current:
            if current.left:
                predecessor = current.left

                while predecessor.right:
                    predecessor = predecessor.right

                predecessor.right = current.right
                current.right = current.left
                current.left = None

            current = current.right