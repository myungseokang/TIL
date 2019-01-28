class Node:
    def __init__(self, data=None):
        # private member
        self._data = data
        self._prev = None
        self._next = None

    @property
    def data(self):
        return self._data
    
    @data.setter
    def data(self, data):
        self._data = data

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, n):
        self._next = n

    @property
    def prev(self):
        return self._prev

    @prev.setter
    def prev(self, p):
        self._prev = p


# ADT
class BaseDeque:
    def push(self, data):
        raise NotImplementedError

    def push_left(self, data):
        raise NotImplementedError

    def pop(self):
        raise NotImplementedError

    def pop_left(self):
        raise NotImplementedError

    def remove(self, data):
        raise NotImplementedError

    def clear(self):
        raise NotImplementedError

    def is_empty(self):
        raise NotImplementedError
    
    def show_all(self):
        raise NotImplementedError


class LinkedDeque(BaseDeque):
    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None

    def push(self, data):
        new_node = Node(data)

        if self.is_empty():
            self.head = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node

        self.tail = new_node
        
        self.size += 1


    def push_left(self, data):
        new_node = Node(data)

        if self.is_empty():
            self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head

        self.head = new_node
        
        self.size += 1

    def pop(self):
        if self.is_empty():
            raise Exception('Deque is empty!')
        
        data = self.tail.data
        self.tail = self.tail.prev
        self.tail.next = None

        self.size -= 1

        return data

    def pop_left(self):
        if self.is_empty():
            raise Exception('Deque is empty!')
        
        data = self.head.data
        self.head = self.head.next
        self.head.prev = None

        self.size -= 1

        return data

    def remove(self, data):
        if self.is_empty():
            raise Exception('Deque is empty!')

        if self.head.data == data:
            self.head = self.head.next
            self.head.prev = None
            self.size -= 1
            return

        elif self.tail.data == data:
            self.tail = self.tail.prev
            self.tail.next = None
            self.size -= 1
            return

        current = self.head.next

        while current.data != data:
            current = current.next

        if current.data is not None:
            current.prev.next = current.next
            current.next.prev = current.prev
            self.size -= 1
        else:
            raise Exception('cannot search')

    def clear(self):
        if self.is_empty():
            raise Exception('Deque is empty!')

        self.head = None
        self.tail = None
        
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def show_all(self):
        current = Node(None)
        current.next = self.head

        while current.next:
            current = current.next
            print(current.data, end=" -> ")
