def generators(n):
    s = set(range(1, n))
    results = []
    for a in s:
        g = set()

        for x in s:
            g.add((a**x) % n)

        if g == s:
            results.append(a)
    return results

g = 7
gens = generators(g)
if gens:
    print(f"Z_{g} has {len(gens)} generators")
    print(f"Z_{g} has generators {gens}")