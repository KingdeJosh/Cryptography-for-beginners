import string
import numpy as np
import math
from sympy import Matrix  # inverse key


# -------------------------
def letterToNumber(letter):
    return string.ascii_lowercase.index(letter)


def numberToLetter(number):
    return chr(int(number) + 97)

# -------------------------

module = 26  # english alphabet

# raw_message = "act"
raw_message = "attack is to night"
print("raw message: ", raw_message)


message = []
key = np.array([
    [3, 10],
    [20, 9]
])  # 2x2
print("We have that the key is ", key)
key_rows = key.shape[0]
key_columns = key.shape[1]

if key_rows != key_columns:
    raise Exception('key must be square matrix!')

# -------Turn letters to numbers----------
print("1. Replace each letter by the number corresponding to its position in the alphabet  ")
for i in range(0, len(raw_message)):
    current_letter = raw_message[i:i + 1].lower()
    if current_letter != ' ':
        letter_index = letterToNumber(current_letter)
        message.append(letter_index)

# -------------------------
print("NB: Message must be multiplier of key line count. if not append beginning of the message to the end")
# if not append beginning of the message to the end

if len(message) % key_rows != 0:
    for i in range(0, len(message)):
        message.append(message[i])
        if len(message) % key_rows == 0:
            break

# ------------------------
# transform message to numpy array. we'll use numpy's matrix multiplication
message = np.array(message)
message_length = message.shape[0]
print("2. We have the message numbers are: ", message)

# transform message array to matrix
message.resize(int(message_length / key_rows), key_rows)
# ------------------------
print("4. Mutiply the enciphering matrix by each plaintext vector mod 26.")
encryption = np.matmul(message, key)
encryption = np.remainder(encryption, module)
encryptions = encryption.flatten()
print("5. The encrypted vector: \n", encryption)
encryption_message = ""
for i in range(0, len(encryptions)):
    letter_num = int(encryptions[i])
    letter = numberToLetter(encryptions[i])
    encryption_message = encryption_message + letter
print("6. Now we convert each entry in the ciphertext vector into its corresponding position in the alphabet: ",
      encryption_message)
# ------------------------

# decryption
# ------------------------
print("To decrypt  ")
print("1. We first find the inverse key")
inverse_key = Matrix(key).inv_mod(module)
inverse_key = np.array(inverse_key)  # sympy to numpy
inverse_key = inverse_key.astype(float)
print("2. The inverse key: ", inverse_key)

# ------------------------
print("3. We validate inverse key. key times inverse key must be a idenity matrix")
check = np.matmul(key, inverse_key)
check = np.remainder(check, module)
print("4. The key times inverse key: ", check)
print("it is ", np.allclose(check, np.eye(2)))

# ------------------------
print("5. To decrypt we mutiply inverse matrix key by encryption cipher ")
decryption = np.matmul(encryption, inverse_key)
decryption = np.remainder(decryption, module)
decryptions = decryption.flatten()
print("6. We then get this decryption matrix: ", decryption)
print("7. Flattening out this matrix we have: ", decryptions)
print("8. We then change numbers to its corresponding text and add it together ")
decrypted_message = ""
for i in range(0, len(decryptions)):
    letter_num = int(decryptions[i])
    letter = numberToLetter(decryptions[i])
    decrypted_message = decrypted_message + letter

print("9. Decrypted message: ", decrypted_message)