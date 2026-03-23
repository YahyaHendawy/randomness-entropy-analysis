import random
import time

# Dataset 1: Python's built-in random number generator
with open("../data/python_random.txt", "w") as f:
    for _ in range(10000):
        f.write(str(random.randint(0, 9)) + "\n")

# Dataset 2: Weak time-based generator
with open("../data/time_random.txt", "w") as f:
    for _ in range(10000):
        num = int(time.time() * 1000) % 10
        f.write(str(num) + "\n")
        time.sleep(0.001)

print("Datasets generated successfully.")
