# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


        
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode()
        tail = dummy

        current1, current2 = list1, list2

        while current1 and current2:
            if current1.val <= current2.val:
                tail.next = current1
                current1 = current1.next
                tail = tail.next
            
            elif current2.val <= current1.val:
                tail.next = current2
                current2 = current2.next
                tail = tail.next

        tail.next = current1 if current1 else current2


        return dummy.next
