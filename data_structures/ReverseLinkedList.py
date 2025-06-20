# Definition for singly-linked list.
# Leet code Problem: https://leetcode.com/problems/reverse-linked-list/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def reverseList(self, head: ListNode) -> ListNode:
        # Initialize a dummy node, which will be the new head after reversal
        dummy_node = ListNode()
        # Start from the head of the list
        current_node = head
        # Iterate over the linked list
        while current_node is not None:
            # Save the next node
            next_node = current_node.next

            # Reverse the link so that current_node.next points to the node before it
            current_node.next = dummy_node.next
            dummy_node.next = current_node

            # Move to the next node in the original list
            current_node = next_node

        # The dummy node's next now points to the head of the reversed list
        return dummy_node.next

    def recursiveReverseList(self, head):
        # Base case: if list is empty or only one node, return head
        if head is None or head.next is None:
            return head
        # Recursively reverse the rest of the list
        new_head = self.recursiveReverseList(head.next)
        # Reverse the current link
        head.next.next = head
        head.next = None
        return new_head

if __name__ == "__main__":
    # Example usage:
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    solution = Solution()

    # reversed_head = solution.reverseList(head)
    reversed_head = solution.recursiveReverseList(head)

    # Print the reversed linked list
    current = reversed_head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")