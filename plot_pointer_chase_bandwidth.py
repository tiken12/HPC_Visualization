import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load CSV
df = pd.read_csv("pointer_chase_perf_results.csv")

# Constants
CPU_FREQ_GHZ = 3.4  #CPU inh MHz 3400.000
CYCLES_PER_SECOND = CPU_FREQ_GHZ * 1e9
BYTES_PER_DOUBLE = 8
OP_PER_ELEMENT = 3  # daxpy: A*x + y = load A, load Y, store Y

# Rename column for consistency
df.rename(columns={'N': 'size'}, inplace=True)

# Estimate time in seconds using cycles and CPU frequency
df['time_sec'] = df['cycles'] / CYCLES_PER_SECOND

# Compute estimated bandwidth
df['computed_bytes'] = df['size'] * OP_PER_ELEMENT * BYTES_PER_DOUBLE
df['computed_bandwidth'] = df['computed_bytes'] / df['time_sec'] / 1e9  # GB/s

# Plot
plt.figure(figsize=(10, 6))
plt.plot(df['size'], df['computed_bandwidth'], label='Estimated Bandwidth (Arithmetic)', marker='o')


plt.axvline(x=4096, color='red', linestyle='--', label='~32KB L1')
plt.axvline(x=128000, color='orange', linestyle='--', label='~1MB L2')
plt.axvline(x=3750000, color='green', linestyle='--', label='~30MB L3')

plt.xlabel("Vector Size (elements)")
plt.ylabel("Bandwidth (GB/s)")
plt.title("Pointer Chase Estimated Bandwidth")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("pointer_chase_bandwidth_plot.png")
plt.show()