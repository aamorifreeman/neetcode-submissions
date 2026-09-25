# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# LINKED LIST QUICK SYNTAX
#
# curr = head              # start at head
# curr.val                 # current node's value
# curr.next                # next node
# curr.next.val            # next node's value
# curr = curr.next         # move forward
#
# while curr:              # traverse until None
# while curr and curr.next:# safe if using curr.next
#
# new = ListNode(val)      # create node
# new.next = curr.next     # point new node to next
# curr.next = new          # insert new after curr
#
# curr.next = curr.next.next   # delete/skip next node

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None
       
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev




        
        