# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast = slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        prev = None
        right = slow.next
        slow.next = None
        while right:
            temp = right.next
            right.next = prev
            prev = right
            right = temp
        
        left, right = head, prev
        while right:
            left_temp, right_temp = left.next, right.next
            left.next = right
            right.next = left_temp
            left, right = left_temp, right_temp