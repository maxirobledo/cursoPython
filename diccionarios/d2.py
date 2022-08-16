counts = dict()
names = ['carlos','jose','mario','jose','jose','mario','martin','juan carlos','jose']
for name in names:
    counts[name] = counts.get(name,0) + 1 
    # if name not in counts:
        # counts[name] = 1 
    # else:
        # counts[name] = counts[name] + 1
print('claves',counts.keys())
print('valores',counts.values())
print('elementos',counts.items())