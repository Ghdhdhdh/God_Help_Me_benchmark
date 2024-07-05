import time

def benchmark():
    start_time = time.time()
    fibonacci_local(10000)
    end_time = time.time()
    return end_time - start_time


def fibonacci_local(n: int):
    fib = [0] * n
    fib[1] = 1
    for i in range(2, n):
        fib[i] = fib[i-1] + fib[i-2]
    return fib