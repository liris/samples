import time

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

if __name__ == "__main__":
    for x in range(3):
        fibonacci(3)
    time.sleep(0)
    start = time.time()
    for x in range(0, 30):
        fibonacci(x)
    end = time.time()
    print end - start
