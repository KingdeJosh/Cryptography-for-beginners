def log(n, k=409):
    d = 262
    i = 1
    g= 21
    print(f"We have that d = {d} p = {k} g={21}\n"
          f"To find log_{g} {d} in Z_{k} we do n = g^i mod {k}\n"
          f"Incrementing i by 1 until we find d == n")
    while n != d :

        n=pow(g,i, k)
        print(f"{g}^{i} (mod {k}) = {n}")
        #print(n, i)
        if n == d:
            print( f"i = {i} which means log_{g} {d} in Z_{k} is {i}")
        i = i+1
log(2)