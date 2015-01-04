import random

def is_success(n):
    arr = [2]*2+[1]*1+[0]*(n-3)
    random.shuffle(arr)
    count2 = 0
    count1 = 0
    for item in arr:
        if item == 2:
            count2 += 1
        elif item == 1:
            count1 += 1
        else:
            continue
        if count2 == 2 and count1 == 0:
            return True
        if count1 ==1:
            return False

if __name__ == "__main__":
    succ = 0
    size = 1000000
    for i in xrange(size):
        if is_success(10):
            succ += 1
    print succ*1.0 / size
