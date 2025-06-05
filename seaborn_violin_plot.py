import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the CSV file
df = pd.read_csv("daxpy_parallel_results.csv")

# Group 1: Very small sizes (1, 5, 10)
small_df = df[df["size"].isin([1, 5, 10])]

# Group 2: Mid sizes (50 to 500)
medium_df = df[(df["size"] >= 50) & (df["size"] <= 500)]

# Group 3: Large sizes (optional)
large_df = df[df["size"] > 500_000]

def plot_violin(data, title):
    plt.figure(figsize=(10, 5))
    sns.violinplot(data=data, x="size", y="bandwidth_GBps", hue="threads", split=True, inner="quartile")
    plt.title(title)
    plt.xlabel("Size (N)")
    plt.ylabel("Bandwidth (GB/s)")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# Plot each group
plot_violin(small_df, "DAXPY Violin Plot (N = 1, 5, 10)")
plot_violin(medium_df, "DAXPY Violin Plot (N = 50 to 500)")
plot_violin(large_df, "DAXPY Violin Plot (N > 500,000)")  # Optional