import math
n= 89701
fac = 2980
e = 1
print(f"When we have n = {n} and Factor = {fac}^2 = {e} mod {n} = ({fac}+{e})({fac}-{e}) = 0 ")

print(f"1. GCD({n},{fac+e}) = {math.gcd(fac+e,n)}\n"
      f"2. Which is a factor of {n} \n")
p = math.gcd(fac+e,n)
q = n/p
print(f"3. q = n/p = {n}/{p} = {q}")
print(f"7. We have that p = {p}  and q = {q}")