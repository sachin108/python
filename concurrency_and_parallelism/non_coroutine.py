import time

def count():
    print("one")
    time.sleep(1)
    print("Two")
    time.sleep(1)

def main():
    for _ in range(3):
        count()

if __name__ ==  "__main__":
    start=time.perf_counter()
    main()
    elapsed=time.perf_counter()-start
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")

'''
one
Two
one
Two
one
Two
coroutine2.py executed in 6.02 seconds.

The count() function prints One and waits for a second, then prints Two and waits for another second. 
'''