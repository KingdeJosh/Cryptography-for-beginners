import random
import math
from Crypto.PublicKey import RSA


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

p = 17
q = 11
print("1. Primes p = ",p," q = ",q)
n = p*q
totient = (p-1)*(q-1)

print("2. n = p * q = ",p,"*",q," = ",n)
print("3. Totient function = (p-1)(q-1) = (",p,"-1)(",q,"-1) = ",totient)

e = random.randint(1, totient)
#e and totient must be coprime

while math.gcd(totient, e) != 1:
	e = random.randint(1, totient)

print(f"4. We then choose e = {e}\n"
	"   We then check if e and totient value are coprimes. \n "
	  f"  To do this we check that gcd({e},{totient}) = 1")



#-------------------------------
#find multiplicative inverse of e mod totient

#brute force
"""d=0
for i in range(totient):
	if (e*i) % totient == 1:
		d = i
		break
"""

d = modInverse(e, totient)

print("5. We then solve for d such that e ·d≡ 1 (mod phi).\n"
	  "   So using inverse modular of (",e,",",totient,")","\n"
		"6. Private key: (",n,",",d,")","Public key: (",n,",",e,")")
publickey = e
privatekey = d

#--------------------------------
m = 14
print("-------------------------")
print("7. Now we want to encrypt the message m = ", m)

ciphertext = pow(m, e, n)
print("8. To do this we have that c = m^e mod n = ",m,"^",e," mod ", n," = ",ciphertext)

print("9. Hence the ciphertext c = ",ciphertext)

restored = pow(ciphertext, d, n)
print("10. To check decryption we compute m = c^d mod n ",ciphertext,"^",d," mod ", n," = ",restored)
if(restored == m):
	print("Thus we get back the message: ",m)
else:
	print("We could not decrypt the message as e or p or q or d are incorrect \nas message= ",m," "
																							  "and decrypted message = ", restored," are not equal")

