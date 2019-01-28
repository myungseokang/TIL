import unittest

from linkedlist import LinkedList


class TestLinkedList(unittest.TestCase):
    def setUp(self):
        self.linked_list = LinkedList()
    
    def test_append(self):
        self.linked_list.append(1)
        self.assertEqual(self.linked_list.size(), 1)

    def test_remove(self):
        self.linked_list.append(1)
        self.linked_list.append(2)
        self.linked_list.append(3)
        self.linked_list.remove(2)
        self.assertEqual(self.linked_list.size(), 2)

    def test_search_by_data(self):
        self.linked_list.append(1)
        self.linked_list.append(2)
        self.linked_list.append(3)
        self.assertEqual(self.linked_list.search_by_data(3), (3, 2))

    def test_search_by_position(self):
        self.linked_list.append(1)
        self.linked_list.append(2)
        self.linked_list.append(3)
        self.assertEqual(self.linked_list.search_by_position(1), 2)


if __name__ == '__main__':
    unittest.main()