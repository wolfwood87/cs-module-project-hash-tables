# Your code here
#exps(x, y, z) =
    #  if x <= 0: y + z
    #  if x >  0: exps(x-1,y+1,z) + exps(x-2,y+2,z*2) + exps(x-3,y+3,z*3)
import time

start_time = time.time()
hash_sequence = {}
def expensive_seq(x, y, z):
    # Your code here
    if x <= 0:
        return y + z
    if f"{x},{y},{z}" in hash_sequence:
        return hash_sequence[f"{x},{y},{z}"]
    else:
        a = expensive_seq(x-1,y+1,z)
        b = expensive_seq(x-2,y+2,z*2)
        c = expensive_seq(x-3,y+3,z*3)
        hash_sequence[f"{x},{y},{z}"] = a + b + c
        return a + b + c


if __name__ == "__main__":
    for i in range(10):
        x = expensive_seq(i*2, i*3, i*4)
        print(f"{i*2} {i*3} {i*4} = {x}")

    print(expensive_seq(150, 400, 800))

end_time = time.time()
print(f"runtime: {end_time-start_time} seconds")
