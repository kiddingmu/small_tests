import random
import time

def find_min(source_list):
    if not source_list:
        return None
    size = len(source_list)
    for i in xrange(0, size):
        minimum  = source_list[i]
        for j in xrange(0, size):
            if minimum > source_list[j]:
                break
        else:
            return minimum

def find_min_linear(source_list):
    if not source_list:
        return None
    minimum = source_list[0]
    for i in xrange(1, len(source_list)):
        if source_list[i] < minimum:
            minimum = source_list[i]
    return minimum

if __name__ == "__main__":
    source = [random.randint(0, 100) for i in xrange(100000)]
    #print source
    time1 = time.time()
    print find_min(source)
    time2 = time.time()
    print "Time", time2 - time1
    print find_min_linear(source)
    time3 = time.time()
    print "Time", time3 - time2
