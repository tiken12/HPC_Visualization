import matplotlib.pyplot as plt
import csv
from collections import defaultdict
import numpy as np

# File to read
csv_file = "pointer_chase_perf_results.csv"

# Prepare storage
perf_data = defaultdict(lambda: defaultdict(list))  # perf_data[N][event] = [values]

with open(csv_file) as f:
    reader = csv.reader(f)
    header = next(reader)
    events = header[2:]  # skip N and trial columns

    for row in reader:
        N = int(row[0])
        for i, event in enumerate(events):
            val = row[i + 2]
            if val != "" and val is not None:
                perf_data[N][event].append(int(val))

# Compute averages
Ns = sorted(perf_data.keys())
avg_results = {event: [] for event in events}

for N in Ns:
    for event in events:
        values = perf_data[N][event]
        avg = np.mean(values) if values else 0
        avg_results[event].append(avg)

# Plotting (you can change which event to visualize)
event_to_plot = "cache-misses"  # change this to any available event
y_values = avg_results[event_to_plot]

plt.figure(figsize=(8, 5))
plt.plot(Ns, y_values, marker='o', linestyle='-', color='blue')
plt.xscale("log")
plt.xlabel("Vector Size (N elements)")
plt.ylabel(f"Average {event_to_plot.replace('-', ' ').capitalize()}")
plt.title(f"{event_to_plot.replace('-', ' ').capitalize()} vs Vector Size")
plt.grid(True, which='both', linestyle='--')
plt.tight_layout()
plt.savefig("plot_pointer_chase_perf.png")
plt.show()