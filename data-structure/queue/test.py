import unittest

from queue import ArrayQueue, LinkedQueue


class TestArrayQueue(unittest.TestCase):
    def setUp(self):
        self.queue = ArrayQueue()

    def test_enqueue(self):
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.queue.enqueue(3)
        self.assertEqual(self.queue.size, 3)

    def test_dequeue(self):
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.assertEqual(self.queue.dequeue(), 1)

    def test_peek(self):
        self.queue.enqueue(1)
        self.assertEqual(self.queue.peek(), 1)

    def test_peek_when_stack_is_empty(self):
        with self.assertRaises(Exception):
            self.queue.peek()
    
    def test_is_empty_when_stack_is_empty(self):
        self.assertEqual(self.queue.is_empty(), True)
    
    def test_is_empty_when_stack_is_not_empty(self):
        self.queue.enqueue(1)
        self.assertEqual(self.queue.is_empty(), False)
    
    def test_show_all(self):
        self.queue.show_all()


class TestLinkedQueue(unittest.TestCase):
    def setUp(self):
        self.queue = LinkedQueue()

    def test_enqueue(self):
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.queue.enqueue(3)
        self.assertEqual(self.queue.size, 3)

    def test_dequeue(self):
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.assertEqual(self.queue.dequeue(), 1)

    def test_peek(self):
        self.queue.enqueue(1)
        self.assertEqual(self.queue.peek(), 1)

    def test_peek_when_stack_is_empty(self):
        with self.assertRaises(Exception):
            self.queue.peek()
    
    def test_is_empty_when_stack_is_empty(self):
        self.assertEqual(self.queue.is_empty(), True)
    
    def test_is_empty_when_stack_is_not_empty(self):
        self.queue.enqueue(1)
        self.assertEqual(self.queue.is_empty(), False)
    
    def test_show_all(self):
        self.queue.show_all()


if __name__ == '__main__':
    unittest.main()
