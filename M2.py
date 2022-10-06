class PriorityQueue:
    def __init__(self, heap):
        self.heap = sorted(heap, reverse=True)
    def __str__(self):
        ispis = str(self.heap[0])+"\n"
        level = 2
        elements = 0
        for i in range(1, len(self)):
            ispis += str(self.heap[i])
            elements += 1
            if elements >= level:
                ispis += "\n"
                elements = 0
                level *= 2
            else:
                ispis += " "
        return ispis
    def __len__(self):
        return len(self.heap)
    def parent(self, i):
        if i == 0 or i >= len(self):
            return -1
        return self.heap[(i-1)/2]

    def left(self, i):
        child = 2 * i + 1
        if child >= len(self):
            return -1
        return child
    def right(self, i):
        child = 2 * i + 2
        if child >= len(self):
            return -1
        return child
    def insert(self, k):
        for i in range(0,len(self)):
            if k > self.heap[i]:
                self.heap.insert(i,k)
                break
    def delete (self, k):
        self.heap.pop(k)
    def get_max(self):
        return self.heap[0]

lista=[3, 8, 1, 10, 11, 4, 2]
pq=PriorityQueue(lista)
pq.insert(5)
# print(len(pq))
print(pq)
pq.delete(5)
print(pq)
print(pq.get_max())
print(pq.left(0))
print(pq.right(2))
