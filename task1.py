class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
        self.lst = iter([])

    def __iter__(self):
        self.start = 0
        self.end = len(self.list_of_list)
        return self

    def get_next_item(self):
        try:
            item = next(self.lst)
        except StopIteration:
            item = 'End_of_list'

        return item

    def __next__(self):
        item = self.get_next_item()

        if item == 'End_of_list':
            if self.start == self.end:
                raise StopIteration

            self.lst = iter(self.list_of_list[self.start])
            item = self.get_next_item()
            self.start += 1

        return item


def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()
