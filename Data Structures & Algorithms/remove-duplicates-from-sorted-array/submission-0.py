class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        s = set()
        for  num in range(nums):
            if num in s:
                remove(num)
            s.add(num)
        return len(num)