import pandas as pd
import matplotlib.pyplot as plt

# Load CSV
df = pd.read_csv("daxpy_parallel_results.csv", header=0)
df.columns = df.columns.str.strip()  # ← removes leading/trailing spaces

# Constants
CPU_FREQ_GHZ = 3.4  # Update based on actual CPU info
CYCLES_PER_SECOND = CPU_FREQ_GHZ * 1e9
BYTES_PER_DOUBLE = 8
OP_PER_ELEMENT = 3  # daxpy: A*x + y

# bandwidth calculations
df['computed_bytes'] = df['size'] * OP_PER_ELEMENT * BYTES_PER_DOUBLE
df['computed_bandwidth'] = df['computed_bytes'] / df['time_sec'] / 1e9  # GB/s

# Plot
plt.figure(figsize=(10, 6))

# Plot each thread count separately
for thread_count in sorted(df['threads'].unique()):
    thread_df = df[df['threads'] == thread_count]
    plt.plot(thread_df['size'], thread_df['computed_bandwidth'],
             marker='o', label=f'{thread_count} thread(s)')

# Cache lines
plt.axvline(x=4096, color='red', linestyle='--', label='L1 (~32KB)')
plt.axvline(x=131072, color='orange', linestyle='--', label='L2 (~1MB)')
plt.axvline(x=3932160, color='green', linestyle='--', label='L3 (~30MB)')

# Final plot formatting
plt.xlabel("Vector Size (elements)")
plt.ylabel("Bandwidth (GB/s)")
plt.title("DAXPY Bandwidth by Thread Count")
plt.grid(True)
plt.legend(loc='center left', bbox_to_anchor=(0.75, 0.5), title="Thread Count")
plt.tight_layout()
plt.savefig("parallel_bandwidth_plot.png")
plt.show()