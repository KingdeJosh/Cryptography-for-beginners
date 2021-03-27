import random

mod = 13 #random.getrandbits(512) #prime
g = 2

print(f"1. Alice and Bob publicly agree to use a modulus p = {mod} and base g = {g}\n")
alicePrivate = 5
alicePublic = pow(g, alicePrivate, mod)
print(f"2. Alice chooses a secret integer a = {alicePrivate}, then sends Bob A = g^a mod p\n"
      f"   A = {g}^{alicePrivate} mod {mod} = {alicePublic}\n"
      f"   Alice public key = {alicePublic}")

bobPrivate = 7
bobPublic = pow(g, bobPrivate, mod)
print(f"3. Bob chooses a secret integer b = {bobPrivate}, then sends Alice B = g^b mod p\n"
      f"   B = {g}^{bobPrivate} mod {mod} = {bobPublic}\n"
      f"   Bob public key = {bobPublic}")

aliceShared = pow(bobPublic, alicePrivate, mod)
bobShared = pow(alicePublic, bobPrivate, mod)

print(f"4. Alice now computes s = B^a mod p\n"
      f"   s = {bobPublic}^{alicePrivate} mod {mod} = {aliceShared}")

print(f"5. Bob now computes s = A^b mod p\n"
      f"   s = {alicePublic}^{bobPrivate} mod {mod} = {bobShared}")

print("6. Alice shared key: ",aliceShared)
print("   Bob shared key: ",bobShared)

print("--------------------")