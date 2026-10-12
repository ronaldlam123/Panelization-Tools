pw, ph, sp = 200, 400, 3

def calc_yield(w, h):
    c1 = int((pw + sp) / (w + sp)) * int((ph + sp) / (h + sp))
    c2 = int((pw + sp) / (h + sp)) * int((ph + sp) / (w + sp))
    max_c = max(c1, c2)
    y = (max_c * w * h) / (pw * ph) * 100
    return max_c, y

target_w, target_h = 22, 93
base_units, base_yield = calc_yield(target_w, target_h)
print(f"BASELINE: {target_w}x{target_h}mm -> {base_units} units ({base_yield:.2f}% yield)\n")

results = []
for w_int in range(150, 300):
    for h_int in range(850, 1050):
        w = w_int / 10.0
        h = h_int / 10.0
        c, y = calc_yield(w, h)
        if y > 85.0:
            results.append((y, w, h, c))

results.sort(reverse=True)

seen_units = set()
filtered = []
for res in results:
    u = res[3]
    if u not in seen_units:
        seen_units.add(u)
        filtered.append(res)
        if len(filtered) == 5:
            break

for res in filtered:
    print(f"| {res[0]:.2f}% | {res[1]:.1f} mm | {res[2]:.1f} mm | {res[3]} |")
