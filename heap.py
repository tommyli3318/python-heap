import heapq

class heap:
    def __init__(self, arr=None, max_heap=False):
        self.heap = []
        self.is_max_heap = max_heap

        if arr:
            assert type(arr) is list, "Argument must be of type list, not %s" % type(arr)
            self.heap = arr[:]
            if self.is_max_heap:
                self.heap = [-x for x in self.heap]
            heapq.heapify(self.heap)

    def push(self, x):
        if self.is_max_heap:
            x = -x
        heapq.heappush(self.heap, x)

    def pop(self):
        res = heapq.heappop(self.heap)
        if self.is_max_heap:
            res = -res
        return res

    def pushpop(self, x):
        if self.is_max_heap:
            x = -x
        res = heapq.heappushpop(self.heap, x)
        if self.is_max_heap:
            res = -res
        return res

    def replace(self, x):
        if self.is_max_heap:
            x = -x
        res = heapq.heapreplace(self.heap, x)
        if self.is_max_heap:
            res = -res
        return res

    def nlargest(self, n):
        res = heapq.nlargest(n, self.heap)
        if self.is_max_heap:
            res = [-x for x in res]
        return res

    def nsmallest(self, n):
        res = heapq.nsmallest(n, self.heap)
        if self.is_max_heap:
            res = [-x for x in res]
        return res
