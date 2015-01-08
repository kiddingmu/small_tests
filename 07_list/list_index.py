import timeit
import random

list_index = timeit.Timer("x[random.randint(0, len(x))]" ,"from __main__ import random, x")

for i in range(1000000, 100000001, 1000000):
    x = list(range(i))
    index_time = list_index.timeit(number=1000)
    print "%15.5f" % index_time
