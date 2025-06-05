import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the raw latency data
df = pd.read_csv("pointer_chase_violin_results.csv")  # Change if you used a different file name

# Optional: Filter large sizes to avoid clutter (e.g., cap at 10 million)
df = df[df["N"] <= 10_000_000]

# Optional: Convert N to string for better x-axis formatting
df["N_str"] = df["N"].apply(lambda x: f"{x:,}")

# Create violin plot
plt.figure(figsize=(14, 6))
sns.violinplot(data=df, x="N_str", y="Latency_ns", scale="width", inner="quartile")

plt.title("Pointer Chase Latency Distribution by N")
plt.xlabel("Size (N)")
plt.ylabel("Latency (ns)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.grid(True)
plt.savefig("pointer_chase_violin.png")
plt.show()