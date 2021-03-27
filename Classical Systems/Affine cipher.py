import string

def preprocessing(m):
    m = m.replace(" ","").replace(",","").replace(".","").replace("'","").replace(":","").replace(";","")
    m = m.lower()
    return m

def lettersOfPlaintext(m):
    letters = []
    for i in range(0, len(m)):
        letters.append(m[i])
    return letters

def letterToNumber(letter):
    return string.ascii_lowercase.index(letter)

def numberToLetter(number):
    return chr(int(number) + 97)

def module(letter_index):
    while (letter_index < 0):
        letter_index += 26

    while (letter_index > 25):
        letter_index -= 26

    return letter_index

print("We have the formular to be s=  ( a * K + b) mod n")
print("NB: a and n must be coprime")
message = "attack to night"
#--------------------------------------------------------
numbermessage = []
print("We have the message to be: ", message)
messages = preprocessing(message)
a=3;b=-4
print("We have that a =",a," and b =",b)
plaintext = lettersOfPlaintext(messages)
#----aphabet to numbers
for i in range(0, len(message)):
    current_letter = message[i:i + 1].lower()
    if current_letter != ' ':
        letter_index = letterToNumber(current_letter)
        numbermessage.append(letter_index)

print("1. Convert letters into its corresponding numbers:", numbermessage)
print("2. Applying the formula we can then encrypt the message as:")
ciphertext = []
for i in plaintext:
    x = letterToNumber(i)
    y = a * x + b
    y = module(y)
    print(f"s = {a} * {x} + ({b})mod 26 = {y}")
    ciphertext.append(numberToLetter(y))
print(ciphertext)

# t = (a*s + b) % n
# s = (t - b)/a

print("To Decrypt")
print("We have the formula to be\nt = (a*s + b) mod n \n  s = (t - b)/a")
print("1. We need to calculate the modular inverse of (a * inv_a) mod n")
def modInverse(a, n=26):
    #(a * inv_a) % n
    for i in range(1, n):
        if (i * a) % n == 1:
            return i
restored_text = []
print("2. Applying the formular we have s= ((t - b)* modInverse(a)) mod n")
for i in ciphertext:
    y = letterToNumber(i)
    #s = (t - b)/a
    mod = modInverse(a)
    x = (y - b)*modInverse(a)
    x = module(x)
    print(f"x = ({y} - ({b})) * {mod} mod 26 = {x}")
    restored_text.append(numberToLetter(x))
print("message is: ", restored_text)

