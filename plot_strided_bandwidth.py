import matplotlib.pyplot as plt
import csv

strides = []
bandwidths = []

with open("daxpy_strided_results.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:
        strides.append(int(row["Stride"]))
        bandwidths.append(float(row["Bandwidth (GB/s)"]))

plt.figure(figsize=(8, 5))
plt.plot(strides, bandwidths, marker='s', linestyle='-', color='orange')
plt.xlabel("Stride")
plt.ylabel("Bandwidth (GB/s)")
plt.title("Strided Access Bandwidth vs. Stride")
plt.grid(True, linestyle='--')
plt.xticks(strides)
plt.tight_layout()
plt.savefig("plot_strided_bandwidth.png")
plt.show()