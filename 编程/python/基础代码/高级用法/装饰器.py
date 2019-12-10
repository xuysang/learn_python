import time

def sum1():
    sum = 1+ 2
    print (sum)

def timeit(func):
    def test():
        start = time.perf_counter()
        func()
        end =time.perf_counter()
        print("time used:", end - start)
    return test

sum1 = timeit(sum1)
sum1()