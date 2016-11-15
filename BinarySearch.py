class BinarySearch(list):
    def __init__(self, length, step):
        super(BinarySearch, self).__init__(range(step, (length * step) + 1, step))
        self.__length = length
        self._step = step
        self._count = 0
        self._upper_bound = length - 1
        self._lower_bound = 0
    @property
    def length(self):
        return self.__length

    def search(self, search_item):
        if self._lower_bound <= self._upper_bound:
            cursor = (self._upper_bound + self._lower_bound) // 2
            if self[cursor] == search_item:
                return {'count': self._count, 'index': cursor}
            elif self[cursor] > search_item:
                self._count += 1
                self._upper_bound = cursor - 1
                return self.search(search_item)
            elif self[cursor] < search_item:
                self._count += 1
                self._lower_bound = cursor + 1
                return self.search(search_item)
        return {'count': self._count, 'index': -1}
print(BinarySearch(100, 10))
print(BinarySearch(100, 10).search(880))
