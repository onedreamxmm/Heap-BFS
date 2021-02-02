import heapq
import random
class Solution:
    def findKthLargest1(self, nums, k):
        return heapq.nlargest(k, nums)[-1]
    # O(k+(n-k)logk) time complexity and O(k) space complexity

    def findKthLargest2(self, nums, k):
        return sorted(nums)[-k]
    # O(nlogn) time complexity and O(1) space complexity

    def findKthLargest3(self, nums, k):
        heap = nums[:k]
        heapq.heapify(heap)
        for x in nums[k:]:
            heapq.heappushpop(heap, x)
        return heap[0]
    # O(k+(n-k)logk) time complexity and O(k) space complexity

    def findKthLargest4(self, nums, k):
        n = len(nums)
        heapq.heapify(nums)
        for i in range(n-k):
            heapq.heappop(nums)
        return nums[0]
    # O(n+(n-k)logn) time complexity and O(n) space complexity

    def findKthLargest5(self, nums, k):
        def partition(low, high):
            i = low - 1
            ran = random.randint(low, high)
            nums[high], nums[ran] = nums[ran], nums[high]
            for j in range(low, high + 1):
                if nums[j] >= nums[high]:
                    i += 1
                    nums[i], nums[j] = nums[j], nums[i]
            return i

        low = 0
        high = len(nums) - 1
        target = k - 1
        while True:
            pivot = partition(low, high)
            if target < pivot:
                high = pivot - 1
            elif pivot < target:
                low = pivot + 1
            else:
                return nums[pivot]
        #time complexity: O(n) in average cases; O(n^2) in the worst cases
        #space complexity: O(1)

if __name__ == "__main__":
    nums = [3, 2, 3, 5, 4, 1]
    o = Solution()
    print(o.findKthLargest1(nums, 2))
    print(o.findKthLargest2(nums, 2))
    print(o.findKthLargest3(nums, 2))
    print(o.findKthLargest4(nums, 2))
    print(o.findKthLargest5(nums, 2))