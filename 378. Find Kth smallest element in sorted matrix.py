'''
Given a n x n matrix where each of the rows and columns are sorted in ascending order, find the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

Example:

matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,

return 13.
Note:
You may assume k is always valid, 1 ≤ k ≤ n2.
'''

import heapq

class Solution:
    def kthSmallest(self, matrix, k):
        minheap = []
        n = len(matrix)

        for r in range(min(k, n)):
            minheap.append((matrix[r][0], r, 0))

        heapq.heapify(minheap)

        while k:
            element, r, c = heapq.heappop(minheap)
            if c < n - 1:
                heapq.heappush(minheap, (matrix[r][c+1], r, c+1))
            k -= 1

        return element

if __name__ == '__main__':
    matrix = [[1, 5, 9],[10, 11, 13],[12, 13, 15]]
    k = 8
    o = Solution()
    print(o.kthSmallest(matrix, k))

'''
Complexity Analysis

Time Complexity: let X=min(K,N); X+Klog(X)

Well the heap construction takes O(X)O(X) time.
After that, we perform KK iterations and each iteration has two operations. We extract the minimum element from a heap containing XX elements. Then we add a new element to this heap. Both the operations will take O(\log(X))O(log(X)) time.
Thus, the total time complexity for this algorithm comes down to be O(X + K\log(X))O(X+Klog(X)) where XX is \text{min}(K, N)min(K,N).
Space Complexity: O(X)O(X) which is occupied by the heap.
'''