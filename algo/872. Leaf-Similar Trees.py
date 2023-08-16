# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        leaf_seq1 = self.get_leaf_seq(root1)
        leaf_seq2 = self.get_leaf_seq(root2)
        return leaf_seq1 == leaf_seq2
    
    def get_leaf_seq(self, root):
        if root == None:
            return []
        if (root.left == None and root.right == None):
            return [root.val]
        l_val = self.get_leaf_seq(root.left)
        r_val = self.get_leaf_seq(root.right)
        return l_val + r_val