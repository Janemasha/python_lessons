class SomeIterator:
    def __iter__(self):
        return SomeIterator(self.limit)


    def __init__(self, limit):
        self.limit = limit
        self.counter = 0


    def __next__(self):
        if self.counter < self.limit:
            self.counter += 1
            return self.counter
        else:
            raise StopIteration


my_iterator = SomeIterator(5)
for item in my_iterator:
    print(item)


for item in my_iterator:
    print(item)

