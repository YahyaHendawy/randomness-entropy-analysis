import matplotlib.pyplot as plt
import math

def analyze(file_path, name):
    with open(file_path) as f:
        data = [int(line.strip()) for line in f]

    counts = [data.count(i) for i in range(10)]

    plt.figure(figsize=(8, 5))
    plt.bar(range(10), counts)
    plt.title(f"{name} Distribution")
    plt.xlabel("Number")
    plt.ylabel("Frequency")
    plt.xticks(range(10))
    plt.savefig(f"../graphs/{name}.png")
    plt.close()

    entropy = 0
    for c in counts:
        p = c / len(data)
        if p > 0:
            entropy -= p * math.log2(p)

    expected = len(data) / 10
    deviations = [abs(c - expected) for c in counts]

    return counts, entropy, deviations
