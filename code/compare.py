from analyze import analyze

python_counts, python_entropy, python_deviations = analyze("../data/python_random.txt", "python_random")
time_counts, time_entropy, time_deviations = analyze("../data/time_random.txt", "time_random")

print("=== Python Random Generator ===")
print("Counts:", python_counts)
print("Entropy:", round(python_entropy, 6))
print("Deviation from expected:", python_deviations)
print()

print("=== Time-Based Generator ===")
print("Counts:", time_counts)
print("Entropy:", round(time_entropy, 6))
print("Deviation from expected:", time_deviations)
