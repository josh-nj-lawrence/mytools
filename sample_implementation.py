from timing import *

### Sample implementation of different Tools
@timeit_avg(15)
def pass_func(n):
    for i in range(n):
        pass

@timeit
@profile
def if_func(n):
    for i in range(n):
        if i == n-1:
            return "Done"


if __name__ == "__main__":
    pass_func(1_000_000)
    if_func(1_000_000)