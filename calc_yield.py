pw, ph, sp = 200, 400, 2
results = []

# Sweep through reasonable module sizes
for w in range(20, 151):
    for h in range(20, 301):
        # Standard orientation
        c1 = int((pw + sp) / (w + sp)) * int((ph + sp) / (h + sp))
        # Rotated orientation
        c2 = int((pw + sp) / (h + sp)) * int((ph + sp) / (w + sp))
        
        max_c = max(c1, c2)
        yield_pct = (max_c * w * h) / (pw * ph) * 100
        
        # Only keep highly efficient sizes
        if yield_pct > 96.0:
            results.append((yield_pct, w, h, max_c))

# Sort by yield percentage (descending)
results.sort(reverse=True)

# Deduplicate to show varied geometries (keep best yield for a roughly similar area)
seen_areas = set()
filtered = []
for res in results:
    area = res[1] * res[2]
    # rough grouping
    area_bin = round(area / 100) * 100
    if area_bin not in seen_areas:
        seen_areas.add(area_bin)
        filtered.append(res)
        if len(filtered) == 15:
            break

print("| Yield % | Module Width | Module Height | Total Units Fit |")
print("|---------|--------------|---------------|-----------------|")
for res in filtered:
    print(f"| {res[0]:.2f}% | {res[1]} mm | {res[2]} mm | {res[3]} |")
