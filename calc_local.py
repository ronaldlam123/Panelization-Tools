pw, ph, sp = 200, 400, 2

def calc_yield(w, h):
    c1 = int((pw + sp) / (w + sp)) * int((ph + sp) / (h + sp))
    c2 = int((pw + sp) / (h + sp)) * int((ph + sp) / (w + sp))
    max_c = max(c1, c2)
    y = (max_c * w * h) / (pw * ph) * 100
    return max_c, y

# Baseline
target_w, target_h = 93, 22
base_units, base_yield = calc_yield(target_w, target_h)
print(f"BASELINE: {target_w}x{target_h}mm -> {base_units} units ({base_yield:.2f}% yield)\n")

print("Nearby Optimized Sizes (+/- 6mm):")
print("| Yield % | Module Width | Module Height | Total Units Fit |")
print("|---------|--------------|---------------|-----------------|")

results = []
# Sweep around the target
for w in range(87, 100):
    # allow sub-millimeter precision for height if needed, but let's stick to 0.1mm steps
    for h_int in range(180, 280): 
        h = h_int / 10.0
        c, y = calc_yield(w, h)
        if y > 85.0:
            results.append((y, w, h, c))

results.sort(reverse=True)

seen_units = set()
filtered = []
for res in results:
    u = res[3]
    # show the best yield for a specific unit count
    if u not in seen_units:
        seen_units.add(u)
        filtered.append(res)
        if len(filtered) == 5:
            break

for res in filtered:
    print(f"| {res[0]:.2f}% | {res[1]} mm | {res[2]:.1f} mm | {res[3]} |")
