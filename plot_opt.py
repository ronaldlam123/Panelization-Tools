import matplotlib.pyplot as plt
import numpy as np
import os

pw, ph, sp = 200, 400, 2

# Create a dense grid around the target dimensions (Width: 15-30, Height: 85-105)
W = np.linspace(15, 30, 300)
H = np.linspace(85, 105, 300)
W_grid, H_grid = np.meshgrid(W, H)

# Calculate yields
C1 = np.floor((pw + sp) / (W_grid + sp)) * np.floor((ph + sp) / (H_grid + sp))
C2 = np.floor((pw + sp) / (H_grid + sp)) * np.floor((ph + sp) / (W_grid + sp))
MaxC = np.maximum(C1, C2)
Yield = (MaxC * W_grid * H_grid) / (pw * ph) * 100

plt.figure(figsize=(9, 7))
# Plot heatmap
heatmap = plt.pcolormesh(W_grid, H_grid, Yield, cmap='plasma', shading='auto', vmin=70, vmax=100)
plt.colorbar(heatmap, label='Area Yield (%)')

# Mark the baseline
plt.plot(22, 93, 'wo', markersize=10, markeredgecolor='black', label='Baseline (22x93, 81.8%)')

# Mark a few key sweet spots
plt.plot(23.1, 99.0, 'go', markersize=10, markeredgecolor='white', label='Optimal 32 Units (23.1x99, 91.5%)')
plt.plot(21.6, 99.0, 'co', markersize=10, markeredgecolor='white', label='Optimal 34 Units (21.6x99, 90.9%)')
plt.plot(20.3, 99.0, 'mo', markersize=10, markeredgecolor='white', label='Optimal 36 Units (20.3x99, 90.4%)')

plt.title('Panelization Yield near 22mm x 93mm', fontsize=14, pad=15)
plt.xlabel('Module Width (mm)', fontsize=12)
plt.ylabel('Module Height (mm)', fontsize=12)
plt.legend(loc='lower left')

# Save to disk
output_path = os.path.join(os.getcwd(), 'yield_optimization_22x93.png')
plt.tight_layout()
plt.savefig(output_path, dpi=200, bbox_inches='tight')
print(output_path)
