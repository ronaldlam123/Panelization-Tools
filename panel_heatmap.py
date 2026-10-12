import matplotlib.pyplot as plt
import numpy as np
import os

# Panel constraints
pw, ph, sp = 200, 400, 2

# Sweep constraints
w_range = np.arange(10, 152, 2)
h_range = np.arange(10, 304, 4)

W, H = np.meshgrid(w_range, h_range)

# Opt 1: Standard orientation
C1 = np.floor((pw + sp) / (W + sp)) * np.floor((ph + sp) / (H + sp))
# Opt 2: Rotated orientation
C2 = np.floor((pw + sp) / (H + sp)) * np.floor((ph + sp) / (W + sp))

MaxC = np.maximum(C1, C2)
Yield = (MaxC * W * H) / (pw * ph) * 100

plt.figure(figsize=(10, 8))
# Plot heatmap
plt.pcolormesh(W, H, Yield, cmap='plasma', shading='auto', vmin=40, vmax=100)
cbar = plt.colorbar(label='Area Yield (%)')

plt.title('Panelization Yield Heatmap (200x400 Panel, 2mm Gap)', fontsize=14, pad=15)
plt.xlabel('Module Width (mm)', fontsize=12)
plt.ylabel('Module Height (mm)', fontsize=12)

# Save to disk
output_path = os.path.join(os.getcwd(), 'panel_heatmap.png')
plt.tight_layout()
plt.savefig(output_path, dpi=200, bbox_inches='tight')
print(output_path)
