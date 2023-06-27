import pyAesCrypt

password = input('enter the password to encrypt the file: ')

# Encrypt

pyAesCrypt.encryptFile('text.txt', 'text1.txt', password)

# Decrypt

password = input('enter the password to dencrypt the file: ')

pyAesCrypt.decryptFile('text1.txt', 'text_decrypt.txt', password)
