import time

def sumOfN3(n):
    start = time.time()
    theSum = n*(n+1)/2
    end = time.time()

    return theSum, end - start

if __name__ == "__main__":
    for i in range(5):
        print "Sum is %d required %10.7f seconds" % sumOfN3(1000000)
