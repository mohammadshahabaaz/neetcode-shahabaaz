class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for j, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                i = seen[complement]
                return [i, j]
            seen[num] = j

        return []