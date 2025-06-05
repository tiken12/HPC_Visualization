import matplotlib.pyplot as plt
import pandas as pd

# Load and clean data
df = pd.read_csv("pointer_chase_cache_profile.csv")
df.columns = df.columns.str.strip()
df["Perf_Bandwidth_GBps"] = df["Perf_Bandwidth_GBps"].fillna(0)

# Average over trials
df_avg = df.groupby("N").mean().reset_index()

# Set up dual Y-axis
fig, ax1 = plt.subplots(figsize=(12, 6))

# App-Derived on left y-axis
color1 = 'tab:blue'
ax1.set_xlabel("Array Size N")
ax1.set_ylabel("App-Derived Bandwidth (GB/s)", color=color1)
ax1.plot(df_avg["N"], df_avg["App_Bandwidth_GBps"], marker='o', linestyle='-', color=color1, label="App-Derived Bandwidth")
ax1.tick_params(axis='y', labelcolor=color1)
ax1.grid(True)

# Perf-Derived on right y-axis
ax2 = ax1.twinx()
color2 = 'tab:orange'
ax2.set_ylabel("Perf-Derived Bandwidth (GB/s)", color=color2)
ax2.plot(df_avg["N"], df_avg["Perf_Bandwidth_GBps"], marker='x', linestyle='--', color=color2, label="Perf-Derived Bandwidth")
ax2.tick_params(axis='y', labelcolor=color2)

# Title and layout
plt.title("Pointer Chase Cache Profile: App vs Perf Bandwidth")
fig.tight_layout()
plt.savefig("pointer_chase_bandwidth_dual_yaxis.png")
plt.show()
