from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def link_to_int(ln: ListNode) -> int:
    """Convert a linked list to an integer."""
    mult = 1
    total = ln.val * mult
    while ln.next is not None:
        ln = ln.next
        mult *= 10
        total += ln.val * mult
    return total


def int_to_link(num: int) -> ListNode:
    """Convert an integer to a linked list."""
    num_list = list(str(num))
    return linkit(num_list)


def linkit(numbers: list) -> ListNode:
    """recursively create linked list from list of numbers."""
    if len(numbers) == 1:
        return ListNode(int(numbers.pop()), None)
    return ListNode(int(numbers.pop()), linkit(numbers))


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        """Sum ListNode numbers."""
        total = 0
        if l1 and l2:
            total = link_to_int(l1) + link_to_int(l2)
        return int_to_link(total)
