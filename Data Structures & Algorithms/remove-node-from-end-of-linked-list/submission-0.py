# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        current = head
        length = 0
        while current:
            length += 1
            current = current.next

        dummy = ListNode(0, head)
        before = dummy

        for _ in range(length - n):
            before = before.next

        before.next = before.next.next

        return dummy.next
        

