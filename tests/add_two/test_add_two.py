from src.add_two.add_two import ListNode, link_to_int, int_to_link, linkit, Solution


class TestSolution:
    """Tests for Solution class."""

    def test_link_to_int(self):
        """Test converting linked list to integer."""
        ln = ListNode(2, ListNode(4, ListNode(3)))
        assert link_to_int(ln) == 342

    def test_int_to_link(self):
        """Test converting integer to linked list."""
        ln = int_to_link(807)
        assert ln.val == 7
        assert ln.next.val == 0
        assert ln.next.next.val == 8
        assert ln.next.next.next is None

    def test_linkit(self):
        """Test recursively creating linked list from list of numbers."""
        ln = linkit(["1", "2", "3"])
        assert ln.val == 3
        assert ln.next.val == 2
        assert ln.next.next.val == 1
        assert ln.next.next.next is None

    def test_add_two_numbers(self):
        """Test adding two numbers represented by linked lists."""
        l1 = ListNode(2, ListNode(4, ListNode(3)))
        l2 = ListNode(5, ListNode(6, ListNode(4)))
        s = Solution()
        result = s.addTwoNumbers(l1, l2)
        assert result.val == 7
        assert result.next.val == 0
        assert result.next.next.val == 8
        assert result.next.next.next is None

    def test_add_two_large_numbers(self):
        """Test adding two large numbers represented by linked lists."""
        l1 = linkit(list("9999999"))
        l2 = linkit(list("9999999"))
        s = Solution()
        result = s.addTwoNumbers(l1, l2)
        assert result.val == 8
        assert result.next.val == 9
        int_result  = link_to_int(result)
        assert int_result == 19999998
