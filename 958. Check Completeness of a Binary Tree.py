'''
Use BFS to do a level order traversal,
add childrens to the bfs queue,
until we met the first empty node.

For a complete binary tree,
there should not be any node after we met an empty one.

Time O(N), Space O(N)

'''

from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isComplete1(self, root: TreeNode) -> bool:
        queue = deque([root])
        l = deque([])
        while queue:
            node = queue.popleft()
            l.append(node)
            if node:
                queue.append(node.left)
                queue.append(node.right)
        for i in range(len(l)):
            if not l[i]:
                for x in range(i+1,len(l)):
                    if l[x]:
                        return False
        return True

    def isComplete2(self, root: TreeNode) -> bool:
        bfs = [root]
        i = 0
        while bfs[i]:
            bfs.append(bfs[i].left)
            bfs.append(bfs[i].right)
            i += 1
        return not any(bfs[i+1:])

if __name__ == '__main__':
    root1 = TreeNode(1)
    root2 = TreeNode(1, TreeNode(2), TreeNode(3))
    root3 = TreeNode(1, TreeNode(2, TreeNode(3)))
    o = Solution()
    print(o.isComplete1(root1))
    print(o.isComplete1(root2))
    print(o.isComplete1(root3))
    print(o.isComplete2(root1))
    print(o.isComplete2(root2))
    print(o.isComplete2(root3))