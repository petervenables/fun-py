"""Tests for ListNode class."""

from src.add_two.add_two import ListNode


class TestListNode:
    """Tests for ListNode class."""

    def test_list_node(self):
        """Test ListNode creation."""
        ln = ListNode(1)
        assert ln.val == 1
        assert ln.next is None

    def test_list_node_next(self):
        """Test ListNode with next."""
        ln2 = ListNode(2)
        ln1 = ListNode(1, ln2)
        assert ln1.val == 1
        assert ln1.next == ln2
        assert ln1.next.val == 2
        assert ln1.next.next is None
