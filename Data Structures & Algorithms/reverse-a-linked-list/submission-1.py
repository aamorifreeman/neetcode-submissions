# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# LINKED LIST QUICK SYNTAX
#
# curr = head              # start at head
# curr.val                 # current node's value
# curr.next                # next node or What does the current node point to?
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
            # Save the next node BEFORE changing curr.next
            # Example: if curr = 1, next_node = 2
            next_node = curr.next

            # Reverse the pointer
            # Example: 1.next = None
            # Next loop: 2.next = 1
            curr.next = prev

            # Move both pointers forward
            prev = curr       # prev now becomes the node we just reversed
            curr = next_node  # curr moves to the original next node

        # curr is now None, and prev is the new head
        return prev


        
        