#Merge a linked list into another linked list at alternate positions.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_alternate(head1: ListNode, head2: ListNode) -> ListNode:
    if not head1:
        return head2
    if not head2:
        return head1
    
    p1 = head1
    p2 = head2
    while p1 and p2:
        # Save next pointers
        p1_next = p1.next
        p2_next = p2.next
        
        # Link p2 node to p1 node
        p1.next = p2
        p2.next = p1_next
        
        # Update pointers for next iteration
        p1 = p1_next
        p2 = p2_next
        
    return head1

# Create first linked list: 1 -> 3 -> 5 -> 7
head1 = ListNode(1)
head1.next = ListNode(3)
head1.next.next = ListNode(5)
head1.next.next.next = ListNode(7)

# Create second linked list: 2 -> 4 -> 6
head2 = ListNode(2)
head2.next = ListNode(4)
head2.next.next = ListNode(6)

# Merge second linked list into first linked list at alternate positions
merged_head = merge_alternate(head1, head2)

# Print merged linked list: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7
while merged_head:
    print(merged_head.val, end=' ')
    merged_head = merged_head.next
