import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Load and clean data
df = pd.read_csv("pointer_chase_cache_profile.csv")
df.columns = df.columns.str.strip()
df["Perf_Bandwidth_GBps"] = df["Perf_Bandwidth_GBps"].fillna(0)

# Optional: Cap N
df = df[df["N"] <= 10_000_000]

# --- Step 1: Cache-size-based binning ---
element_size = 8  # bytes per element

# Define bin edges in bytes
bins_bytes = [
    0,
    32 * 1024,         # L1
    256 * 1024,        # L2
    4 * 1024 * 1024    # L3
]

# Add a dynamic final bin edge if needed
max_bytes = df["N"].max() * element_size
if max_bytes > bins_bytes[-1]:
    bins_bytes.append(max_bytes + 1)

# Convert to element count
bins = sorted(set([b // element_size for b in bins_bytes]))  # unique & sorted
labels = ["L1", "L2", "L3", "Beyond L3"][:len(bins) - 1]

# Assign bins with 'duplicates' handling
df["Size_Bin"] = pd.cut(df["N"], bins=bins, labels=labels, include_lowest=True, duplicates='drop')
df = df.dropna(subset=["Size_Bin"])

# --- Step 2: Prepare data for violin plot ---
df_violin = pd.melt(
    df,
    id_vars=["Size_Bin"],
    value_vars=["App_Bandwidth_GBps", "Perf_Bandwidth_GBps"],
    var_name="Bandwidth_Type",
    value_name="Bandwidth_GBps",
    ignore_index=False
)

df_violin["Bandwidth_Type"] = df_violin["Bandwidth_Type"].replace({
    "App_Bandwidth_GBps": "App-Derived",
    "Perf_Bandwidth_GBps": "Perf-Derived"
})

# --- Step 3: Plot ---
sns.set(style="whitegrid", font_scale=1.4)
plt.figure(figsize=(14, 8))

sns.violinplot(
    data=df_violin,
    x="Size_Bin",
    y="Bandwidth_GBps",
    hue="Bandwidth_Type",
    scale="width",
    inner="quartile",
    bw=0.3,
    cut=0,
    palette={"App-Derived": "#1f77b4", "Perf-Derived": "#ff7f0e"}
)

plt.title("Pointer Chase Bandwidth by Cache-Level Size (L1, L2, L3, Beyond)", fontsize=18)
plt.xlabel("Estimated Cache Bin (based on memory footprint)", fontsize=14)
plt.ylabel("Bandwidth (GB/s)", fontsize=14)
plt.legend(title="Bandwidth Type", loc="upper right", fontsize=12, title_fontsize=13)
plt.grid(True, axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()

# Save and display
plt.savefig("Pointer_Chase_Bandwidth_Violin_CacheBins.png", dpi=300)
plt.show()
