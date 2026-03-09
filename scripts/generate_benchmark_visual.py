import matplotlib.pyplot as plt

# Using the performance data we established
labels = ['64-Core CPU\n(Legacy Solver)', 'NVIDIA A100\n(GPU Accelerated)', 'AI Surrogate\n(NVIDIA-First)']
times = [12600, 12.2, 0.12] # Representing 3.5 hrs, 12s, and 120ms

plt.style.use('dark_background') # Matches the NVIDIA 'Green on Black' aesthetic
fig, ax = plt.subplots(figsize=(12, 7))

# High-contrast colors for storytelling
colors = ['#4A4A4A', '#76b900', '#00ffcc']
bars = ax.bar(labels, times, color=colors, edgecolor='white', linewidth=1.5)

ax.set_yscale('log') # Essential to visualize the 105,000x difference
ax.set_ylabel('Execution Time (Seconds) - Log Scale', fontsize=12, color='#76b900')
ax.set_title('The Generational Leap: O(n³) Solving vs. O(1) Inference', fontsize=18, fontweight='bold', pad=25)

# Add data labels on top of bars
for bar in bars:
    height = bar.get_height()
    ax.annotate(f'{height:,.2f}s',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 8), textcoords="offset points",
                ha='center', va='bottom', fontsize=12, fontweight='bold', color='white')

plt.grid(axis='y', linestyle='--', alpha=0.2)
plt.tight_layout()

# This saves the file to the Colab 'Files' sidebar
plt.savefig('performance_benchmark.png', dpi=300, bbox_inches='tight')
plt.show()
