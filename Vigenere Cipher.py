
english_alpha = "abcdefghijklmnopqrstuvwxyz"
def enc_message(instruction,message, key):
    cipher_or_message = ""
    key_position = [] # key index ie: when k='d' then key_position= 3
    for letter in key:
        key_position.append(english_alpha.find(letter))
    number = 0
    for letter in message:
      if number == len(key_position):
          number = 0
      if instruction == '1':# encrypt
        index = english_alpha.find(letter) + key_position[number] #get  character index and shift with the key
        if index > 25:
            index = index-26               # use modulus
        cipher_or_message += english_alpha[index].capitalize()  #make cipher always capital letters
        number +=1
      elif instruction == '2':#decrypt
          position = english_alpha.find(letter.lower()) - key_position[number]
          if position < 0:
              position = position + 26
          cipher_or_message += english_alpha[position].lower()
          number += 1
      else:
          print("Please enter e valid choice!")
    return cipher_or_message

try:
    print("Welcome to vigenere cipher --Joshua Akujobi.\n\n"
          "Enter 1 for Encryption e message \nenter 2 for Decryption")
    p = input("How do we proceed (1/2): ")
    message = input("Whats your message or cipher?: ")
    message = message.replace(" ", "")  # no space in the message
    if message.isalpha():
        key = input("Input key: ")
        key = key.strip()  # rno space in the key
        if key.isalpha():
            cipher = enc_message(p,message, key)
            print("The cipher or message is: ", cipher)
        else:
            print(key)
            print("Enter valid key, key is only one character word!")
    else:
        print("only letters are allowed !!")

except Exception as e:
    print(e)
    exit("Enter e valid text please! ")