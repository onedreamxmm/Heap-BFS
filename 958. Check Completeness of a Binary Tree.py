'''
Use BFS to do a level order traversal,
add childrens to the bfs queue,
until we met the first empty node.

For a complete binary tree,
there should not be any node after we met an empty one.

Time O(N), Space O(N)
'''


class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isCompleteTree(self, root):
        bfs = [root]
        i = 0
        while bfs[i]:
            bfs.append(bfs[i].left)
            bfs.append(bfs[i].right)
            i += 1
        return not any(bfs[i: ])

if __name__ == '__main__':
    root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, None, TreeNode(7)))
    o = Solution()
    print(o.isCompleteTree(root))