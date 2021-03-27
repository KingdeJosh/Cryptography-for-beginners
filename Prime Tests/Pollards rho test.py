from random import randint
import math

def is_probably_prime(n, k=1000):
    print(f"1. We want to factor n = {n}")
    a=2
    b=a
    z=3
    print(f"2. We know that a = b = {a}")
    print(f"3. Using the function f(x) = x^2 + {z}\n"
          f"   We can compute a = a^2 + {z} (mod n)\n"
          f"   b = ((b^2)+  {z})^2 + {z}) (mod n)\n"
          f"   d = gcd(a-b, n) (mod n)")
    print(f"4. Putting in the values we have")
    for i in range(k):
        print(f"   a = {a}^2 + {z} (mod {n})\n"
              f"   b = ((({b}^2)+  {z})^2) + {z}) (mod {n})\n")
        a = (pow(a,2)+z) % n
        b = (pow((pow(b,2)+z), 2)+z) % n
        d = math.gcd(a-b,n) % n
        print(f"   d = gcd({a}-{b}, {n}) (mod {n}) = {d}")

        if 1<d<n:
            print(f"5. if 1<d<n then p = d and q = n/p\n"
                  f"   We have that 1<{d}<{n}  ")
            p=d
            q=n/p
            return print("6. So p=",p,f", q={n}/{p} = {q}")


is_probably_prime(1027)