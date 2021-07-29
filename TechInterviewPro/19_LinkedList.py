from typing import List


class ListNode:
    def __init__(self,data):
        self.data = data
        self.next = None

    def __str__(self):
        node = self
        output = ""
        # print (len(node))
        while node!= None:
            # print  (node.data)
            output += str(node.data) + " "
            node = node.next
        return output

    def __len__(self):
        len = 0
        node = self
        while node != None:
            len += 1
            node = node.next
        return len 

def insert_at_begin(ll,val):
    new_node = ListNode(val)
    new_node.next = ll
    return new_node

def insert_at_end(ll,val):
    head = ll
    node = ll
    while node.next!= None :
        node = node.next

    node.next = ListNode(val)
    return head 

def insert_at_middle(ll,index,val):
    head = ll
    node = ll
    curr_index = 0
    while node != None:
        if curr_index == index:
            break
        node = node.next
        curr_index += 1

    new_node = ListNode(val)
    new_node.next = node.next  
    node.next = new_node

    return head 

def delete_node(ll,index):
    head = ll
    node = ll
    curr_index = 0
    while node != None:
        if curr_index == index:
            break
        node = node.next
        curr_index += 1
    node.data = node.next.data
    node.next = node.next.next
    return ll

def reverse_ll(ll):
    # 1 - 2 - 3 - 765 - 5 - None
    # None - 1 - 2 - 3 - 765 - 5
    prev = None
    curr = ll
    #print  (len(ll))
    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
        #print  (curr.data, prev.data, prev.next,curr.next)
    return prev 


def list2linkedlist(l):
    if l == []: return None

    head = ListNode(l[0])
    n = head
    count = 0
    for i in range(1,len(l)):
        new = ListNode(l[i])
        n.next = new
        n = n.next

    return head 

if __name__ =='__main__':
    l1 = [1,2,3,4,5]
    l2 = [2,3,45,6,9]

    n1 = list2linkedlist(l1)
    n2 = list2linkedlist(l2)
     
    print  (n1)
    print  (n2)

    n3 = insert_at_begin(n1,999)
    print  (n3)

    n4 = insert_at_end(n1,876)
    print  (n4)

    n5 = insert_at_middle(n4,3,765)
    
    print  (n5) 
    print  (len(n5))

    n6 = delete_node(n5,3)
    print  (n6)

    n7 = reverse_ll(n1)
    print  (n7)