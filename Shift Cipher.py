# Shift Cipher
No_of_Alpha = 26

def bruteForce(plaintext, k):
    bruteForce = ''
    k = -k

    for letter in plaintext:
        if letter.isalpha():
            shift = ord(letter)
            shift += k
            if letter.islower():
                if shift > ord('z'):
                    shift -= 26
                elif shift < ord('e'):
                    shift += 26
            elif letter.isupper():
                if shift > ord('Z'):
                    shift -= 26
                elif shift < ord('A'):
                    shift += 26

            bruteForce += chr(shift)
        else:
            bruteForce += letter
    return bruteForce


print('Whats is your cipher?')
plaintext = input()

for k in range(1, No_of_Alpha + 1):
    print('Possible key ', k, ':', bruteForce(plaintext, k))