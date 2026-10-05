# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        curr = head
        prev = None

        while curr:
            next_node = curr.next #save next node
            curr.next = prev #point curr to prev/ reverse step
            prev = curr #move prev
            curr = next_node #stand on next node/move forward
        return prev
        

        
        