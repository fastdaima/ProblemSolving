# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

# Return the head of the merged linked list.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, first: Optional[ListNode], second: Optional[ListNode]) -> Optional[ListNode]:
        
        head = ListNode(-1)

        dummy = head 

        while first and second:
            if first.val <= second.val:
                dummy.next = first
                first = first.next
            else:
                dummy.next = second 
                second = second.next
            dummy = dummy.next 
        
        if first or second: 
            dummy.next = first if first else second

        return head.next