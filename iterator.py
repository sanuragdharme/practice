class Iterator:

    def __init__(self):
        self.num = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.num <= 10:
            val = self.num
            self.num += 1

            return val
        else:
            raise StopIteration


number = Iterator()

print(number.__next__())
print(next(number))

for i in number:
    print(i, end=" ")
