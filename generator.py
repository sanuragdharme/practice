# Yield is a special keyword which makes function generator

def generate():

    yield 5
    yield 1
    yield 4
    yield 2
    yield 3


values = generate()

print(next(values))
print(next(values))

for i in values:
    print(i)


def perfect_square():
    num = 1

    while num <= 10:
        square = num * num
        yield square
        num += 1


values = perfect_square()
for i in values:
    print(i, end=" ")