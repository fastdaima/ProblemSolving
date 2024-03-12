# reverse a list 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return head
        ll = []
        while head:
            ll.append(head)
            head = head.next 
        
        head = ListNode(-1)
        dummy = head

        while ll:
            node  = ll.pop()
            head.next = node
            head = head.next
            
        head.next = None 
        return dummy.next



# optimized
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev=None
        cur=head
        while cur:
            nxt=cur.next
            cur.next=prev
            prev=cur
            cur=nxt
        head=prev
        return head

        