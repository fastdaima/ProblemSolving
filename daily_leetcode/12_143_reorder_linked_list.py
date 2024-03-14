
# You are given the head of a singly linked-list. The list can be represented as:

# L0 → L1 → … → Ln - 1 → Ln
# Reorder the list to be on the following form:

# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
# You may not modify the values in the list's nodes. Only nodes themselves may be changed.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# appending nodes to list 
# finding cutoff point, if it is even it is len - (len/2 -1) else len - (len/2), because if length is 4 only last element we can able to insert
# ex: 
# i/p: a -> b -> c -> d -> e 
# o/p: a -> e -> b -> d -> c 
# cutoff point at index 3 i.e) d 
# iterate through left and right pointers
# until right pointer meets cutoff point
# pop rightmost node
# assign rightmost_node.next = leftmost_node.next
# then assign leftmost_node.next = rightmost_node


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        dummy = head 

        nodes = []

        len_ = 0 

        while dummy: 
            nodes.append(dummy)
            dummy = dummy.next 
        
        len_ = len(nodes)


        left = 0 
        right = len_ - 1

        cutoff_point = len_ - ((len_//2)-1 if len_ % 2 == 0 else len_//2) - 1


        while right != cutoff_point:

            left_node = nodes[left]
            right_node = nodes[right]

            right_node.next = left_node.next
            left_node.next = right_node


            left += 1
            right -= 1

        nodes[right].next = None         
