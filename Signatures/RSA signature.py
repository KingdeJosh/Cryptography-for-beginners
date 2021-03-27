import math
import random
from Crypto.PublicKey import RSA
import hashlib

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

p = 13
q = 17
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
	  f"  To do this we check that gcd(",e,",",totient,f") = 1  which we have it to be {math.gcd(totient, e)}")



#-------------------------------
#find multiplicative inverse of e mod totient

d = modInverse(e, totient)

print("5. We then solve for d such that e ·d≡ 1 (mod phi).\n"
	  "   So using inverse modular of (",e,",",totient,")","\n"
		"6. Private key: (",n,",",d,")","Public key: (",n,",",e,")")
publickey = e
privatekey = d

message = 5

#hashHex = hashlib.sha256(message).hexdigest()
#message = int(hashHex, 16)

#print("message: ",message)

signature =pow(message, privatekey, n)
print(f"7. Alice now signs the message ({message}) as follows ({message}^{privatekey} mod {n}) to get :")
print("   signature: ",signature)

#alice sends bob message, signature
#--------------------------------

decryptedSignature = pow(signature, publickey, n)
print("8. Bob now decrypts Alice signature dS = S_A^e mod n:\n"
      f"   = {signature}^{publickey} mod {n} = {decryptedSignature}")
print("9. Alice decrypted Signature: ",decryptedSignature)

if message == decryptedSignature:
	print(f"10. Signature is valid as Alice encrypted signed message {message} = "
          f"bob encryption of alice signature with \nalice public key to get {decryptedSignature} ")
else:
	print("signature is not valid!!!")

#--------------------------------

