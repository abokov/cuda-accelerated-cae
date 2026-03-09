import matplotlib.pyplot as plt

# Using the results from your benchmark
labels = ['64-Core CPU\n(Classical)', 'NVIDIA A100\n(Accelerated)', 'AI Surrogate\n(NVIDIA-First)']
times = [12600, 12.2, 0.12] # Representing 3.5 hrs, 12s, and 120ms

plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(10, 6))

# NVIDIA Green and complementary colors
colors = ['#4A4A4A', '#76b900', '#00ffcc']
bars = ax.bar(labels, times, color=colors, edgecolor='white', linewidth=1.2)

ax.set_yscale('log') # This is CRITICAL to show the 100,000x difference
ax.set_ylabel('Execution Time (Seconds) - Log Scale', fontsize=12, color='#76b900')
ax.set_title('The Generational Leap: O(n³) Solving vs. O(1) Inference', fontsize=16, fontweight='bold', pad=20)

# Add data labels on top of bars
for bar in bars:
    height = bar.get_height()
    ax.annotate(f'{height:,.2f}s',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 5), textcoords="offset points",
                ha='center', va='bottom', fontsize=11, fontweight='bold')

plt.grid(axis='y', linestyle='--', alpha=0.3)
plt.tight_layout()

# Save the figure
plt.savefig('performance_benchmark.png', dpi=300, transparent=False)
plt.show()
