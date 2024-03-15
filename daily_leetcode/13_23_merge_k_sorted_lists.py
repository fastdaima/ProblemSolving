# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

# Merge all the linked-lists into one sorted linked-list and return it.

 

# Example 1:

# Input: lists = [[1,4,5],[1,3,4],[2,6]]
# Output: [1,1,2,3,4,4,5,6]
# Explanation: The linked-lists are:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# merging them into one sorted list:
# 1->1->2->3->4->4->5->6
# Example 2:

# Input: lists = []
# Output: []
# Example 3:

# Input: lists = [[]]
# Output: []

class Solution:
    def merge2Lists(self, first: Optional[ListNode], second: Optional[ListNode]) -> Optional[ListNode]:
        
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

        # print(head)
        return head.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        if not lists: return None

        prev_node = lists[0] 

        for i in range(1, len(lists)):
          
            prev_node = self.merge2Lists(prev_node, lists[i])
        
        return prev_node

            
# [TOADD] 
# Heap Version