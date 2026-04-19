        right = head
            right = right.next
            n -= 1
        dummy.next = head
        
        while n > 0:
        
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev = dummy = ListNode()
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
        left = dummy
        
        while right:
            left = left.next
            right = right.next

        left.next = left.next.next

        return dummy.next