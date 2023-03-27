from time import time as perf_counter
from memory_profiler import profile # Memory profile wrapper
import random

# Timing wrapper
def timeit(method):
    def wrapper(*arg, **kw):
        t = perf_counter()
        ret = method(*arg, **kw)
        print('Method ' + method.__name__ + ' took : ' +
              "{:2.5f}".format(perf_counter()-t) + ' sec')
        return ret
    return wrapper

# Average Timing wrapper
def timeit_avg(itterations: int =10):
    def deco(method):
        def wrapper(*args, **kw):
            results = [0]*itterations
            for i in range(itterations):
                t = perf_counter()
                ret = method(*args, **kw)
                results[i] = perf_counter() - t
            print('Method ' + method.__name__ + ' took : ' +
                  '{:2.5f}'.format(sum(results)/itterations) + 
                  ' sec on average over {} itterations'.format(itterations))
            return ret
        return wrapper
    return deco

if __name__ == "__main__":
    @timeit
    def test_method():
        print("Test")
    test_method()