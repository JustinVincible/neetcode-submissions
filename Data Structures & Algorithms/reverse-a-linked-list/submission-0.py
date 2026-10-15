# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        seen_vals = []
        if head is None:
            return None
        cur_node = head
        cur_val = head.val
        while cur_node.next is not None:
            cur_val = cur_node.val
            seen_vals.append(cur_val)
            cur_node = cur_node.next
        
        new_head = ListNode(cur_node.val)
        cur_node = new_head
        for val in seen_vals[::-1]:
            cur_node.next = ListNode(val)
            cur_node = cur_node.next

        #print(f"seen_vals: {seen_vals}")

        return new_head