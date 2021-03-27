import math
import random
from Crypto.Random import get_random_bytes
from Crypto.PublicKey import ElGamal
def modInverse(number, mod):
	x1 = 1;
	x2 = 0;
	x3 = mod
	y1 = 0;
	y2 = 1;
	y3 = number

	q = int(x3 / y3)

	t1 = x1 - q * y1
	t2 = x2 - q * y2
	t3 = x3 - q * y3

	while y3 != 1:
		x1 = y1;
		x2 = y2;
		x3 = y3
		y1 = t1;
		y2 = t2;
		y3 = t3

		q = int(x3 / y3)
		t1 = x1 - q * y1
		t2 = x2 - q * y2
		t3 = x3 - q * y3

	if y2 < 0:
		while y2 < 0:
			y2 = y2 + mod

	return y2

p = 2357  # prime
"""config = ElGamal.generate(512, get_random_bytes)
p = getattr(config, 'p')"""
g = 2
s = random.randint(1, p - 2)
t = pow(g, s, p)

print(f"1. We choose a value s from 1 to p - 2: s = {s}\n"
      f"   t = g^s mod p = {g}^{s} mod {p} = {t}")
print("2. We have that public key: (p=", p, ", g=", g, ", t=", t, ")")
print("   private key: ", s)

# ------------------------------
# digital signatures

print(" \nSigning")

message = 146
print(f"3. We then choose a message = {message}")
k = random.randint(1, p - 1)
print(f"4. Alice selects randomly k ∈ (1,p-1) such that its gcd(k,p-1) = 1\n"
      f"   k = {k} and gcd({k},{p-1}) = {math.gcd(k,p-1)}")

while math.gcd(p - 1, k) != 1:
    k = random.randint(1, p - 1)
y = pow(g, k, p)
a = (message - s * y) * modInverse(k, p - 1) % (p - 1)
print("5. Alice computes γ = g^k(mod p) and a = k^(−1) * (message − s * y) (mod p − 1)\n"
      f"   y = {g}^{k} (mod {p})\n"
      f"   a = {k}^(-1)*({message} - {s} * {y}) (mod {p} - 1)")

print("6. signature: (y=", y, ", a=", a, ")")

message = 146

checkpoint1 = pow(g, message, p)
checkpoint2 = (pow(t, y, p) * pow(y, a, p)) % p
print("7. To verify we will make two checks verification as follows\n"
      "   check1 = (t^y * y^a) = g^message (mod p)\n"
      "   check2 = (t^y * y^a) = t^y * (g^k)^a (mod p)")
print(f"8. We have that check1 = {g}^{message} (mod {p})\n"
      f"   check2 = {t}^{y} * ({g}^{k})^{a} (mod {p})")
print("   check1: ", checkpoint1)
print("   check2: ", checkpoint2)

if checkpoint1 == checkpoint2:
    print("9. check1 = check2 so signature is valid")
else:
    print("invalid signature detected")

print("-----------------------")