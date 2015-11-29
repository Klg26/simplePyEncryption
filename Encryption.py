# Imported Libraries
import random
import numpy as np
import readline

#Enable Paste Feature
readline.parse_and_bind("control-v: paste")

# Open File
f = open('Info.txt', 'w+')

# Giving Characters A Value
characters = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h':8, 'i': 9, 'j': 10, 'k': 11, 'l': 12,
              'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23,
              'x': 24, 'y': 25, 'z': 26, ' ': 27, '  ': 28, ':': 29, '(': 30, ')': 31, '1': 32,
              '2': 33, '3': 34, '4': 35, '5': 36, '6': 37, '7': 38, '8': 39, '9': 40, '0': 41, '.': 42, '!': 43,
              ',': 44, ';': 45, '@': 46}

# User Input
message = input('Enter Message: ').lower()
# Declare Required Variables For Loop
messageL = (len(message))
x = 0
encryptionMessage = []

# Changes Characters To Character Value
while (x < messageL):
    encryptionMessage.append(str(characters.get(message[x])))
    x += 1

# Generate Secret Key
encryptionKey=[]
for i in range(messageL):
    encryptionKey.append(random.randrange(1, 101, 1))

# Encrypt The Message
encryptionMessage = list(map(int, encryptionMessage))
fEncryptionMessage = list(np.array(encryptionMessage) + np.array(encryptionKey))

# Print Info To Screen And File
print("Encryption Key: ", file=f)
print("Encryption Key: ")
print(str(encryptionKey)[1:-1])
f.write("%s\n" % encryptionKey)
print("Your Message: ", file=f)
print("Your Message: ")
print(str(fEncryptionMessage)[1:-1])
f.write("%s\n" % fEncryptionMessage)
print("Information successfully saved to Info.txt file.")

# Close File
f.close()

# Close Program
closeInput = input("Press ENTER to exit")
print("Closing...")
