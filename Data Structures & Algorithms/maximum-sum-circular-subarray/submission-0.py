class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total = sum(nums)
        curMax = maxSum = nums[0]
        curMin = minSum = nums[0]
        for num in nums[1:]:
            curMax = max(num, curMax + num)
            curMin = min(num, curMin + num)

            maxSum = max(maxSum, curMax)
            minSum = min(curMin, minSum)

        if maxSum < 0:
            return maxSum
        return max(maxSum, total - minSum)