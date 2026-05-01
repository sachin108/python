# Measuring Execution Time
from time import perf_counter, sleep

class Timer:
    def __enter__(self):
        self.start = perf_counter()

    def __exit__(self, *_):
        end = perf_counter()
        print(f"Elapsed time: {end - self.start:.4f} seconds")