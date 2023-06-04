class Item:
    def __init__(self, name):
        self._name = name

    def __str__(self):
        return f"{self._name}"


class Array:
    def __init__(self, items):
        self._items = items

    def __iter__(self):
        return ArrayIterator(self)

    def get_item(self, index):
        return self._items[index]

    def get_count(self):
        return len(self._items)


class ArrayIterator:
    def __init__(self, array):
        self._array = array
        self._index = -1

    def __next__(self):
        self._index += 1
        if self._index >= self._array.get_count():
            raise StopIteration
        return self._array.get_item(self._index)


items = [Item(name= 1), Item(name= 2), Item(name= 3), Item(name= 4)]

array = Array(items)

# iterator
for item in array:
    print(str(item))

# 1
# 2
# 3
# 4

# generator
def array_generator(iter = array):
    for item in iter:
        yield str(item)

gen = array_generator()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

# 1
# 2
# 3
# 4
