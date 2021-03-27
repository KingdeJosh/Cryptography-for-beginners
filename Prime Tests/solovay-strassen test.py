import math
from random import randint

def solovay():
    n = 17
    a = randint(0, n)
    print(f"1. Select random a; a = {a}")
    b = math.gcd(a,n)
    print(f"2. We compute b = gcd(a,n) = gcd({a},{n}) = {b}")
    print(f"If gcd(a,n) > 1 ")
    for i in range(5):
        if b > 1:
            return print(f"3. We check if b > 1. \n"
                         f"   Since {b}> 1 then {n} is probably not prime")
        s = round(a/n)
        d = pow(a,round((n-1)/2),n)

        print(f"3. compute s =  a/n = {a}/{n}={s} and\n"
              f"   d = a^((n-1)/2) (mod n) = {a}^(({n}-1)/2) (mod {n}) = {d}\n"
              f"   >>>>>>>>Iteration: {i}<<<<<<<<<<<<<<<\n"
              f"   We check if s not equal to d.")
        if s != d:
            return print(f"4. Since {s} is not equal to {d} then {n} is probably not prime")
    return print(f"4. After {n} itreations we can say that {n} is probably Prime")

solovay()