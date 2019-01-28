import random


class MinHeap:
    def __init__(self):
        # 루트노드를 1번부터 시작하게끔 0번은 비워둠
        self.queue = [None]

    @staticmethod
    def get_parent_idx(index):
        # 완전이진트리이기 떄문에 가능한 연산
        return index // 2
    
    @staticmethod
    def get_leftchild_idx(index):
        return index * 2
    
    @staticmethod
    def get_rightchild_idx(index):
        return index * 2 + 1
    
    def get_last_idx(self):
        return len(self.queue) - 1

    def swap(self, x, y):
        self.queue[x], self.queue[y] = self.queue[y], self.queue[x]
    
    def min_heapify(self, index):
        left = self.get_leftchild_idx(index)
        right = self.get_rightchild_idx(index)
        min_val = index

        if left <= self.get_last_idx() and self.queue[left] < self.queue[min_val]:
            min_val = left
        if right <= self.get_last_idx() and self.queue[right] < self.queue[min_val]:
            min_val = right

        if min_val != index:
            self.swap(index, min_val)
            self.min_heapify(min_val)

    def insert(self, data):
        self.queue.append(data)
        last_idx = self.get_last_idx()

        while last_idx > 1:
            parent_idx = self.get_parent_idx(last_idx)
            if self.queue[last_idx] < self.queue[parent_idx]:
                self.swap(last_idx, parent_idx)
                last_idx = parent_idx
            else:
                break

    def delete(self):
        self.swap(1, self.get_last_idx())
        self.queue.pop(self.get_last_idx())
        self.min_heapify(1)
    
    def show_all(self):
        # 더 이쁘게 출력은 안되나... ㅠㅠ
        height = 1
        for idx, val in enumerate(self.queue[1:]):
            if idx + 1 == 2 ** height:
                print('')
                height += 1

            print(val, end=', ')

        print(' ')


if __name__ == '__main__':
    min_heap = MinHeap()

    for _ in range(10):
        min_heap.insert(random.randint(1, 50))
    min_heap.show_all()
