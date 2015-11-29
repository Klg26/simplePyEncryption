# Imported Libraries
import numpy as np
import readline

#Enable Paste Feature
readline.parse_and_bind("control-v: paste")

characters = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h', 9: 'i', 10: 'j', 11: 'k', 12: 'l',
              13: 'm', 14: 'n', 15: 'o', 16: 'p', 17: 'q', 18: 'r', 19: 's', 20: 't', 21: 'u', 22: 'v', 23: 'w',
              24: 'x', 25: 'y', 26: 'z', 27: ' ', 28: '  ', 29: ':', '(': 30, ')': 31, 32: '1',
              33: '2', 34: '3', 35: '4', 36: '5', 37: '6', 38: '7', 39: '8', 40: '9', 41: '0', 42: '.', 43: '!',
              44: ',', 45: ';', 46: '@'}

# Open File
f = open('Results.txt', 'w+')

# User Input
encryptionKey = input('Enter Encryption Key: ')
encryptionMessage = input('Enter Encryption Message: ')

encryptionKeyList = encryptionKey.split(",")
encryptionMessageList = encryptionMessage.split(",")

encryptionMessageList = list(map(int, encryptionMessageList))
encryptionKeyList = list(map(int, encryptionKeyList))

decryptedMessage = list(np.array(encryptionMessageList) - np.array(encryptionKeyList))

decryptedL= (len(decryptedMessage))
x = 0
message = []

while (x < decryptedL):
    message.append(str(characters.get(decryptedMessage[x])))
    x += 1

# Print Info To Screen And File
print(''.join(message))
f.write(''.join(message))
print("Information successfully saved to Info.txt file.")
# Close File
f.close()
# Close Program
closeInput = input("Press ENTER to exit")
print("Closing...")