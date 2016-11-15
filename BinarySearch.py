class BinarySearch(list):
    def __init__(self, list_length, step):
        try:
            self._num_list = range(step, (list_length * step) + 1, step)
            list.__init__(self, self._num_list)
            self.__length = list_length
        except TypeError:
            self._num_list = []
            list.__init__(self, self._num_list)

    @property
    def length(self):
        return len(self._num_list)

    def search(self, search_item):
        found = False
        count = 0
        self._upper_bound = self.length - 1
        self._lower_bound = 0
        if not self._num_list:
            return 'Given Input Parameters are invlaid'
        elif search_item not in self._num_list:
            return {'count': count, 'index' : -1}
        else:
            if self._lower_bound <= self._upper_bound and not found:
                cursor = (self._upper_bound + self._lower_bound) // 2

                if self._num_list[self._upper_bound] == search_item:
                    return {'count': count, 'index': self._upper_bound}
                elif self._num_list[self._lower_bound] == search_item:
                    return {'count': count, 'index': self._lower_bound}
                elif self._num_list[cursor] == search_item:
                    count += 1
                    found = True
                elif self._num_list[cursor] > search_item:
                    count += 1
                    self._upper_bound = cursor - 1
                elif self._num_list[cursor] < search_item:
                    count += 1
                    self._lower_bound = cursor + 1
        return {'count': count, 'index': self._num_list.index(search_item)}


def main():
    #
    print(BinarySearch(100, {}).search(4))
    print(BinarySearch(100, 10).search(880))
    print(BinarySearch(20, 2).search(40))

if __name__ == '__main__':main()