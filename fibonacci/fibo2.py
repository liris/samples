import time

def fibonacci(n):
    value = 0
    f1 = 1
    f2 = -1
    for i in range(n+1):
        value = f1 + f2
        f2 = f1
        f1 = value
    
    return value

if __name__ == "__main__":
    for x in range(3):
        fibonacci(3)
    time.sleep(0)
    start = time.time()
    for x in range(0, 5000):
        fibonacci(x)
    end = time.time()
    print end - start
