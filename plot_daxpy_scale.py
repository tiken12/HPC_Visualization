import matplotlib.pyplot as plt
import csv

sizes = []
bandwidths = []

with open("daxpy_scale_results.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:
        sizes.append(int(row["Size"]))
        bandwidths.append(float(row["Bandwidth (GB/s)"]))

plt.figure(figsize=(8, 5))
plt.plot(sizes, bandwidths, marker='o', linestyle='-', color='blue')
plt.xscale("log")
plt.xlabel("Vector Size (Elements)")
plt.ylabel("Bandwidth (GB/s)")
plt.title("DAXPY Bandwidth vs. Vector Size")
plt.grid(True, which='both', linestyle='--')
plt.tight_layout()
plt.savefig("plot_daxpy_scale.png")
plt.show()