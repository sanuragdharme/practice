# In the Anonymous function, we can pass n no of arguments but it should be of one expression
# Filter Map Reduce
from functools import reduce

nums = [3, 2, 6, 8, 4, 6, 2, 9]
# Filter large chunk of data
evens = list(filter(lambda num: num % 2 == 0, nums))

# Perform some operations
doubles = list(map(lambda num: num * 2, evens))

# Reduce it
addition = reduce(lambda a, b: a + b, doubles)
print(addition)
