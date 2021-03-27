from random import randint

def is_probably_prime(n, k=1):

    d = n - 1
    s = 0
    ifsetter = 1
    print(f"1. We have that n = {n}, k-times: k = {k} and d = {n-1}")
    print(f"2. We then make an iteration until d is not divisible by 2")
    while not d % 2:
        s += 1
        d //= 2


    for i in range(k):
        a = randint(2, n - 2)
        x = pow(a, d, n)
        print("3. We Pick a random number 'a' in range [2, n-2]\n"
              f"   a = {a}")
        print("4. We then Compute: x = a^d (mod n)\n"
              f"   x = {a}^{d} (mod {n}) = {x}")
        print(f"5. We then check to see if x = 1 or (n-1). \n")

        if x == 1 or x == (n - 1):

            if x==1:
                print(f"  we see that x = {x}")
            elif x==(n-1):
                print(f"   we see that x = (n-1) = {n}")
            continue
        print(f"6. We then compute x^2 (mod n)")
        for _ in range(s - 1):
            print(f"   x = {x}^2 (mod {n})")
            x = pow(x, 2, n)
            print(f"   = {x}")
            if x == (n - 1):
                print(f"7. We see x is equal to (n-1) i.e. {x} = {n-1}")
                break
        else:
            return print(f"6. As x is not equal to 1 or {n-1}\n"
                         f"   {n} is Not prime")

    return print(f"   So {x} Probably prime")
is_probably_prime(172)