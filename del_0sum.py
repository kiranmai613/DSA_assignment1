class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def remove_zero_sum_sublists(head: ListNode) -> ListNode:
    dummy = ListNode(0)
    dummy.next = head
    seen = {0: dummy}
    curr = head
    prefix_sum = 0

    while curr:
        prefix_sum += curr.val

        if prefix_sum in seen:
            node_to_remove = seen[prefix_sum].next
            prefix_sum_to_remove = prefix_sum + node_to_remove.val

            while prefix_sum_to_remove != prefix_sum:
                del seen[prefix_sum_to_remove]
                node_to_remove = node_to_remove.next
                prefix_sum_to_remove += node_to_remove.val

            seen[prefix_sum].next = curr.next
        else:
            seen[prefix_sum] = curr

        curr = curr.next

    return dummy.next
# Create the linked list 1 -> 2 -> -3 -> 3 -> 1
node1 = ListNode(1)
node2 = ListNode(-1)
node3 = ListNode(3)
node4 = ListNode(3)
node5 = ListNode(1)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

# Call the remove_zero_sum_sublists function with the head of the linked list
new_head = remove_zero_sum_sublists(node1)

# Iterate over the modified linked list and display the output
curr = new_head
while curr:
    print(curr.val, end=" ")
    curr = curr.next
