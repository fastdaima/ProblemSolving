# Given the head of a linked list, remove the nth node from the end of the list and return its head.

 

# Example 1:


# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]
# Example 2:

# Input: head = [1], n = 1
# Output: []
# Example 3:

# Input: head = [1,2], n = 1
# Output: [1]
 

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        if not head.next:
            return None
        dummy = head 
        len_ = 0 
        
        while head: 
            len_ += 1 
            head = head.next 
        
        target = len_ - n 


        
        head = dummy
        dummy = ListNode(-1)
        dummy.next = head

        head = dummy 

        len_ = -1

        while head: 
            len_ += 1 
            if len_ == target:
                head.next = head.next.next 
                break
            head = head.next 
        
        return dummy.next


# optimized
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow = fast = dummy = ListNode(-1, head)

        for _ in range(n + 1):
            fast = fast.next

        while fast is not None:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next if slow.next is not None else None

        return dummy.next


        

