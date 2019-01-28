# ADT
class BaseQueue:
    def enqueue(self, data):
        """데이터 넣기"""
        raise NotImplementedError
    
    def dequeue(self):
        """데이터 꺼내기"""
        raise NotImplementedError
    
    def peek(self):
        """맨 앞의 데이터 보기"""
        raise NotImplementedError
    
    def is_empty(self):
        """
        데이터 유무 검사
        있으면 False, 없으면 True
        """
        raise NotImplementedError
    
    def show_all(self):
        """모든 데이터를 보여줌"""
        raise NotImplementedError


class ArrayQueue(BaseQueue):
    def __init__(self):
        self.items = []
        self.size = 0
        self.front = 0
        self.rear = 0
    
    def enqueue(self, data):
        self.items.append(data)
        self.size += 1
        self.rear += 1

    def dequeue(self):
        if self.is_empty():
            raise Exception('Queue is empty!')
    
        data = self.items[self.front]
        self.front += 1
        self.size -= 1
        
        return data

    def peek(self):
        if self.is_empty():
            raise Exception('Queue is empty!')
        
        return self.items[self.front]
    
    def is_empty(self):
        return self.size == 0
    
    def show_all(self):
        for index in range(self.front, self.rear):
            print(self.items[index])


class Node:
    def __init__(self, data=None):
        # private member
        self._data = data
        self._next = None

    def __del__(self):
        print(f'데이터 {self.data} 삭제됨')
    
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

class LinkedQueue(BaseQueue):
    def __init__(self):
        self.size = 0
        self.front = None
        self.rear = None
    
    def enqueue(self, data):
        new_node = Node(data)
        
        if self.is_empty():
            self.front = new_node
        else:
            self.rear.next = new_node
        self.rear = new_node

        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise Exception('Queue is empty!')

        first_node = self.front
        self.front = self.front.next
        self.size -= 1

        if self.is_empty():
            self.rear = None
        
        return first_node.data
    
    def peek(self):
        if self.is_empty():
            raise Exception('Queue is empty!')

        return self.front.data

    def is_empty(self):
        return self.size == 0
    
    def show_all(self):
        current = Node(None)
        current.next = self.front

        while current.next:
            current = current.next
            print(current.data)
