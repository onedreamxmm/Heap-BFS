'''
Approach 2: Iteration  BFS
Algorithm

Let's keep nodes of each tree level in the queue structure, which typically orders elements in a FIFO (first-in-first-out) manner. In Java one could use LinkedList implementation of the Queue interface. In Python using Queue structure would be an overkill since it's designed for a safe exchange between multiple threads and hence requires locking which leads to a performance loose. In Python the queue implementation with a fast atomic append() and popleft() is deque.

The zero level contains only one node root. The algorithm is simple :

Initiate queue with a root and start from the level number 0 : level = 0.

While queue is not empty :

Start the current level by adding an empty list into output structure levels.

Compute how many elements should be on the current level : it's a queue length.

Pop out all these elements from the queue and add them into the current level.

Push their child nodes into the queue for the next level.

Go to the next level level++.

Time complexity : O(N) since each node is processed exactly once.

Space complexity : O(N) to keep the output structure which contains N node values.
'''

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque
class Solution:
    def levelOrder(self, root):
        if not root:
            return None
        queue = deque([root])
        res = []
        while queue:
            size = len(queue)
            list = []
            for i in range(size):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                list.append(node.val)
            res.append(list)
        return res


if __name__ == '__main__':
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    o = Solution()
    print(o.levelOrder(root))

