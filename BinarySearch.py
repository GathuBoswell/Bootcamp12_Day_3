class BinarySearch(list):

    def __init__(self, length, step):
        self.__length = length
        self._step = step

        for x in range(self.__length):
            list.append(self, self._step)
            self._step += step

    @property
    def length(self):
        return self.__length

print(BinarySearch(10, 1))
