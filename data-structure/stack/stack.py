# ADT
class BaseStack:
    def push(self, data):
        """데이터 저장하기"""
        raise NotImplementedError

    def pop(self):
        """데이터 꺼내기"""
        raise NotImplementedError

    def peek(self):
        """맨 위의 데이터 보기"""
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


class Stack(BaseStack):
    def __init__(self):
        self.items = []
        self.top = 0
    
    def push(self, data):
        self.items.append(data)
        self.top += 1
    
    def pop(self):
        if self.is_empty():
            raise Exception('Stack is empty!')

        self.top -= 1
        data = self.items[self.top]
        del self.items[self.top]

        return data

    def peek(self):
        if self.is_empty():
            raise Exception('Stack is empty!')
            
        return self.items[self.top - 1]
    
    def is_empty(self):
        return self.top == 0
    
    def show_all(self):
        for idx in range(self.top):
            print(self.items[idx])
