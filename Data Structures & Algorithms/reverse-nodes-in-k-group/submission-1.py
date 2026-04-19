# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def getKCandidate(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        while k > 0 and head:
            k -= 1
            head = head.next
        
        return head

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        prevKGroup = dummy = ListNode(0, next=head)
        print(prevKGroup.val, prevKGroup.next.val)

        while prevKGroup:
            KCandidate = self.getKCandidate(prevKGroup, k)
            if KCandidate is None:
                break
            groupNext = KCandidate.next
            print("KCandidate", KCandidate.val)
            
            prev, curr = KCandidate.next, prevKGroup.next
            while curr != KCandidate:
                temp = curr.next
                curr.next = prev

                prev = curr
                curr = temp
                print(prev.val, curr.val)
            
            print(prevKGroup.val, prevKGroup.next.val)
            temp_head = prevKGroup.next

            curr.next = prev
            prevKGroup.next = curr
            prevKGroup = temp_head
        
        return dummy.next
        
