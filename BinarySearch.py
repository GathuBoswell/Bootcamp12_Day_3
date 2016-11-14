class BinarySearch(list):

    def __init__(self, length, step):
        super().__init__()
        self.__length = length
        self._step = step
        self._count = 0
        self._upper = length
        self._lower = 0

        for x in range(self.__length):
            list.append(self, self._step)
            self._step += step

    @property
    def length(self):
        return self.__length

    def search(self, search_item):
        cursor = (self._upper + self._lower) // 2
        if self[cursor] == search_item:
            return {'count': self._count, 'index': cursor}
        elif self[cursor] > search_item:
            self._upper = cursor - 1
            self._count += 1
            return self.search(search_item)
        elif self[cursor] < search_item:
            self._lower = cursor + 1
            self._count += 1
            return self.search(search_item)

print(BinarySearch(10, 1))
print(BinarySearch(10, 1).search(2))
