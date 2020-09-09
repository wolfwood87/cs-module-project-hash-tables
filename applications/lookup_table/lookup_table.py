# Your code here
import math
import random
import time

start_time = time.time()
hash_slow_fun = {}

def slowfun_too_slow(x, y):
    v = math.pow(x, y)
    v = math.factorial(v)
    v //= (x + y)
    v %= 982451653

    return v

def slowfun(x, y):
    if f"{x},{y}" in hash_slow_fun:
        return hash_slow_fun[f"{x},{y}"]
    else:
        v = math.pow(x, y)
        v = math.factorial(v)
        v //= (x + y)
        v %= 982451653
        hash_slow_fun[f"{x},{y}"] = v
        return v
    """
    Rewrite slowfun_too_slow() in here so that the program produces the same
    output, but completes quickly instead of taking ages to run.
    """
    # Your code here



# Do not modify below this line!

for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')

end_time = time.time()
print(f"runtime: {end_time-start_time} seconds")