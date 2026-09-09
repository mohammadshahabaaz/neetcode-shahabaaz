# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        cur = head
        arr = []
        while cur:
            arr.append(cur.val)
            cur = cur.next

        maxSum = 0
        curSum = 0
        L, R = 0, len(arr) - 1
        while L < R:
            curSum = arr[L] + arr[R]
            maxSum = max(curSum, maxSum)
            L += 1
            R -= 1
        return maxSum