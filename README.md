# PCB Panelization Optimization Tools

This repository contains a suite of interactive, HTML/Plotly-based tools and Python scripts for optimizing PCB panelization. These tools calculate the maximum number of modules that can fit on a manufacturing panel and generate heatmaps of area yield.

## Included Tools
* **`dynamic_heatmap.html`**: A fully interactive Yield Explorer. Adjust panel dimensions, handling borders, routing gaps, and module size sweeps dynamically in the browser.
* **`side_by_side.html`**: Side-by-side comparison of different length optimizations.
* **`heatmap_combined_labels.html`**: Master heatmap showing all key constraints and optimized "sweet spots".
* **`l_shape_layout.html` / `mixed_grid_final.html`**: Visualizers for complex panel layouts (interlocking L-shapes and mixed vertical/horizontal rotated grids).

## Usage
Simply open any of the `.html` files in a web browser (Safari, Chrome, Firefox) to view the interactive plots and layouts. No local web server or Python environment is required to run the HTML tools.

*(Python scripts are also included for headless calculation and matrix generation).*
