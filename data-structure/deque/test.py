import unittest

from deque import LinkedDeque


class TestLinkedDeque(unittest.TestCase):
    def setUp(self):
        self.deque = LinkedDeque()

    def test_push(self):
        self.deque.push(1)
        self.deque.push(2)
        self.deque.push(3)
        self.assertEqual(self.deque.size, 3)
    
    def test_push_left(self):
        self.deque.push_left(1)
        self.deque.push_left(2)
        self.deque.push_left(3)
        self.assertEqual(self.deque.size, 3)

    def test_pop(self):
        self.deque.push(1)
        self.deque.push(2)
        self.deque.push(3)
        self.assertEqual(self.deque.pop(), 3)
        self.assertEqual(self.deque.size, 2)

    def test_pop_left(self):
        self.deque.push(1)
        self.deque.push(2)
        self.deque.push(3)
        self.assertEqual(self.deque.pop_left(), 1)
        self.assertEqual(self.deque.size, 2)

    def test_remove(self):
        self.deque.push(1)
        self.deque.push(2)
        self.deque.push(3)
        self.deque.remove(1)
        self.assertEqual(self.deque.size, 2)
    
    def test_clear(self):
        self.deque.push(1)
        self.deque.push(2)
        self.deque.push(3)
        self.assertEqual(self.deque.size, 3)
        self.deque.clear()
        self.assertEqual(self.deque.size, 0)

    def test_is_empty(self):
        self.assertEqual(self.deque.is_empty(), True)


if __name__ == '__main__':
    unittest.main()
