class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_k_group(head: ListNode, k: int) -> ListNode:
    curr, prev, next_ = head, None, None
    count = 0

    # Count the number of nodes in the current group
    while curr and count < k:
        curr = curr.next
        count += 1

    # Base case: If there are fewer than k nodes left, don't reverse
    if count < k:
        return head

    # Reverse the current group of k nodes
    curr = head
    for i in range(k):
        next_ = curr.next
        curr.next = prev
        prev = curr
        curr = next_

    # Recursively reverse the remaining groups of k nodes
    head.next = reverse_k_group(next_, k)

    return prev

# Create a linked list: 1 -> 2 -> 3 -> 4 -> 5
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

# Reverse the linked list in groups of 2 nodes
head = reverse_k_group(head, 3)

# Display the reversed linked list
while head:
    print(head.val, end=' ')
    head = head.next



