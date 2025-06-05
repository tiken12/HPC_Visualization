import matplotlib.pyplot as plt
import csv

sizes = []
times = []

with open("pointer_chase_results.csv") as f:
    reader = csv.reader(f)
    next(reader)  # ✅ Skip header row
    for row in reader:
        sizes.append(int(row[0]))
        times.append(float(row[2]))  # Assuming column 2 is Avg Time

# Compute access rate: 1 / time per access
access_rate = [1 / t for t in times]

plt.figure(figsize=(8, 5))
plt.plot(sizes, access_rate, marker='^', linestyle='-', color='green')
plt.xscale("log")
plt.xlabel("Vector Size (Elements)")
plt.ylabel("Access Rate (1 / sec)")
plt.title("Pointer Chase: Access Rate vs. Vector Size")
plt.grid(True, which='both', linestyle='--')
plt.tight_layout()
plt.savefig("plot_pointer_chase.png")
plt.show()