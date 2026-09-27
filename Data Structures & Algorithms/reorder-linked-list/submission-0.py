# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        array = []
        current = head
        while current:
            array.append(current)
            current = current.next

        left = 0
        right = len(array) - 1

        while left < right:
            array[left].next = array[right]
            array[right].next = array[left+1]
            left += 1
            right -= 1


        array[left].next = None


        