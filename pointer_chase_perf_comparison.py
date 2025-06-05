import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load CSV file
df = pd.read_csv("pointer_chase_perf_validated.csv")
df.columns = df.columns.str.strip()

# Group by N to compute average over trials
grouped = df.groupby("N").agg({
    "Latency_ns": "mean",
    "App_Bandwidth_GBps": "mean",
    "Perf_Bandwidth_GBps": "mean"
}).reset_index()

# 1. Latency Plot
plt.figure(figsize=(12, 5))
sns.lineplot(data=grouped, x="N", y="Latency_ns", marker="o", linewidth=2)
plt.title("Pointer Chase: Average Latency per Array Size (N)")
plt.xlabel("Array Size N")
plt.ylabel("Latency (ns)")
plt.grid(True, linestyle=":")
plt.tight_layout()
plt.savefig("pointer_chase_latency.png")
print("✅ Saved: pointer_chase_latency.png")

# 2. Bandwidth Comparison Plot with Dual Y-Axis
fig, ax1 = plt.subplots(figsize=(12, 5))

color1 = "tab:blue"
ax1.set_xlabel("Array Size N")
ax1.set_ylabel("App-Derived Bandwidth (GB/s)", color=color1)
ax1.plot(grouped["N"], grouped["App_Bandwidth_GBps"], marker="o", color=color1, label="App-Derived")
ax1.tick_params(axis='y', labelcolor=color1)
ax1.grid(True, linestyle=":")

ax2 = ax1.twinx()  # second y-axis
color2 = "tab:orange"
ax2.set_ylabel("Perf-Derived Bandwidth (GB/s)", color=color2)
ax2.plot(grouped["N"], grouped["Perf_Bandwidth_GBps"], marker="x", linestyle="--", color=color2, label="Perf-Derived")
ax2.tick_params(axis='y', labelcolor=color2)

plt.title("Pointer Chase: Bandwidth Comparison")
fig.tight_layout()
plt.savefig("pointer_chase_bandwidth_comparison_dual_axis.png")
print("✅ Saved: pointer_chase_bandwidth_comparison_dual_axis.png")

plt.show()
