import unittest

from stack import Stack


class TestLinkedList(unittest.TestCase):
    def setUp(self):
        self.stack = Stack()
    
    def test_push(self):
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)
        self.assertEqual(self.stack.top, 3)
    
    def test_pop(self):
        self.stack.push(1)
        self.stack.push(2)
        self.assertEqual(self.stack.pop(), 2)
        self.assertEqual(self.stack.top, 1)
    
    def test_pop_when_stack_is_empty(self):
        with self.assertRaises(Exception):
            self.stack.pop()
    
    def test_peek(self):
        self.stack.push(1)
        self.assertEqual(self.stack.peek(), 1)
        self.assertEqual(self.stack.top, 1)

    def test_peek_when_stack_is_empty(self):
        with self.assertRaises(Exception):
            self.stack.peek()
    
    def test_is_empty_when_stack_is_empty(self):
        self.assertEqual(self.stack.is_empty(), True)
    
    def test_is_empty_when_stack_is_not_empty(self):
        self.stack.push(1)
        self.assertEqual(self.stack.is_empty(), False)
    
    def test_show_all(self):
        self.stack.show_all()


if __name__ == '__main__':
    unittest.main()