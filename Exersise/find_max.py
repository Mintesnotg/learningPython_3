
from time import time
import random

def find_max(data):
    biggest = data[0]  # The initial value to beat
    for val in data:  # For each value:
        if val > biggest:  # if it is greater than the best so far,
            biggest = val  # we have found a new best (so far)
    return biggest  # When loop ends, biggest is the max

n = 1000000
rand_data = random.sample(range(1, n + 1), n)  # Random permutation
sorted_data = list(range(1, n + 1))  # Sorted order

# sor=sorted(n)

start = time()
find_max(rand_data)
end = time()
elapsed=end-start

print(f"Elapsed time for random data: {elapsed:.6f} seconds")

order_start=time()
find_max(sorted_data)
order_end=time()
elapsed_ordered=order_end - order_start

print(f"Elapsed time for sorted data: {elapsed_ordered:.6f} seconds")


