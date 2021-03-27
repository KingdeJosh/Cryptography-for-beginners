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

p = 47  # prime
"""config = ElGamal.generate(512, get_random_bytes)
p = getattr(config, 'p')"""
g = 5
x = random.randint(1, p - 2)
y = pow(g, x, p)

print(f"1. We choose a value x from 1 to p - 2: x = {x}\n"
      f"   h = g^x mod p = {g}^{x} mod {p} = {y}")
print("2. We have that public key: (p=", p, ", g=", g, ", h=", y, ")")
print("   private key: ", x)
# Bob knows g, p, t
m = 17
print(f"3. We then need to encrypt the message = {m}")
k = random.randint(1, p - 1)
print(f"4. To do this we have to choose a value k from 1 to p-1: \n"
      f"   k = {k}")
s = pow(y, k, p)
print(f"5. We then compute the shared secret value s = h^k mod p = {y}^{k} mod {p} = {s} ")

c1 = pow(g, k, p)
c2 = m * s % p
print(f"6. Finally we encrypt the message to obtain two cipher texts c1 and c2\n"
      f"   c1 = g^k mod p = {g}^{k} mod {p} = {c1}\n"
      f"   c2 = m * s mod p = {m} * {s} mod {p} = {c2}")

print("7. Ciphertext: (c1=", c1, ", c2=", c2, ")")

# bob sends c1, c2 pair to alice

print("\nDecryption")
restored = c2 * pow(c1, (p - 1 - x), p) % p
print(f"1. To decrypt the message we simply compute the following\n"
      f"   m = c2 * (c1^(p - 1 - x) mod p) mod p\n"
      f"   m = {c2} * ({c1}^({p} - 1 - {x}) mod {p}) mod {p} = {restored}")

print("2. restored message: ", restored)

# ------------------------------
# digital signatures

print("-----------------------")
print("digital signature")
print("-----------------------")

print("signing")

hash = 100

k = random.randint(1, p - 1)

while math.gcd(p - 1, k) != 1:
    k = random.randint(1, p - 1)

# print("random key: ",k)

r = pow(g, k, p)
s = (hash - x * r) * modInverse(k, p - 1) % (p - 1)

print("signature: (y=", r, ", s=", s, ")")

print("verification")

hash = 100

checkpoint1 = pow(g, hash, p)
checkpoint2 = (pow(y, r, p) * pow(r, s, p)) % p

print("checkpoint1: ", checkpoint1)
print("checkpoint2: ", checkpoint2)

if checkpoint1 == checkpoint2:
    print("signature is valid")
else:
    print("invalid signature detected")

print("-----------------------")