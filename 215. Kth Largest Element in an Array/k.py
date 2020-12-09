class Solution:
    def findKthLargest(self, nums, k):
        return sorted(nums)[-k]

if __name__ == "__main__":
    nums = [3.1, 2, 3, 5.5, 4.2, 1]
    o = Solution()
    print(o.findKthLargest(nums, 2))