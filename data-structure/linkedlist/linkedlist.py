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


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def is_empty(self):
        return True if self.length == 0 else False

    def size(self):
        return self.length
    
    def append(self, data):
        # 새로운 노드를 추가하는 경우
        new_node = Node(data)

        if self.is_empty():
            # 비었을 경우
            self.head = new_node
            self.tail = new_node
            self.length += 1
        else:
            # 데이터가 한개이상 있을 경우
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1
    
    def search_by_data(self, target, start=0):
        """
        start 부터 target 과 일치하는 데이터를 찾고, 해당 데이터와 위치를 튜플로 묶어서 반환
        target 이 존재하지 않으면 None, None 반환
        """
        if self.is_empty():
            return None
        
        pos = 0
        current = self.head

        if pos >= start and target == current.data:
            return current.data, pos

        while current.next:
            pos += 1
            current = current.next

            if pos >= start and target == current.data:
                return current.data, pos

        return None, None

    def search_by_position(self, pos):
        """
        pos 위치에 해당하는 노드의 데이터를 반환
        pos 가 범위를 벗어나거나 음의 값일 경우 None 반환
        """
        if self.is_empty() or self.size() - 1 < pos:
            # pos 가 리스트의 범위를 벗어나는 경우
            return None
        
        count = 0
        current = self.head

        if count == pos:
            return current.data
            
        while count < pos:
            current = current.next
            count += 1

            if count == pos:
                return current.data
        
        return None

    def remove(self, target):
        if self.is_empty():
            return None
        
        before = self.head
        current = self.head

        if target == current.data:
            if self.size() == 1:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
            
            self.length -= 1
            return current.data
        
        while current.next:
            current = current.next
            before = current
            
            if target == current.data:
                if current == self.tail:
                    self.tail = before
                
                before.next = current.next
                self.length -= 1
                return current.data
        
        return None
