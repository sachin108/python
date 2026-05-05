import time
from multiprocessing import Process

COUNT = 50_000_000

def countdown(n):
    while n > 0:
        n -= 1

if __name__ == '__main__':
    # Single-threaded baseline
    start = time.time()
    countdown(COUNT)
    print(f"Single: {time.time() - start:.4f}s") # 0.9456s

    # Multiprocess
    p1 = Process(target=countdown, args=(COUNT//2,))
    p2 = Process(target=countdown, args=(COUNT//2,))
    start = time.time()
    p1.start(); p2.start()
    p1.join(); p2.join()
    print(f"Multiprocess: {time.time() - start:.4f}s") # 0.5461s