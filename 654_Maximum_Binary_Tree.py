# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        maxVal = max(nums)
        maxNode = TreeNode(maxVal)
        leftSub, rightSub = nums[:nums.index(maxVal)], nums[nums.index(maxVal)+1:]
        leftNode = self.constructMaximumBinaryTree(leftSub)
        maxNode.left = leftNode
        rightNode = self.constructMaximumBinaryTree(rightSub)
        maxNode.right = rightNode
        return maxNode