#libraries needed for the encryption
from Crypto.Cipher import AES
import binascii
import sys

#Contains the secrect IV
#import mySecrectIV

#Secret 16-char key
KEY = "A9sDFua8sdfI112x"
IV = "aBokiaBokiaBokil" #16 character string

#workaround zero_IV
zero_iv = ''.join([chr(0) for i in range(16)])

#Encryption function
def encrypt(message, key):
    aes = AES.new(key, AES.MODE_CBC, zero_iv)
    return aes.encrypt(message)

#Decryption function
def decrypt(message, key):
    aes = AES.new(key, AES.MODE_CBC, zero_iv)
    return aes.decrypt(message)

#xor two strings and return a string
def sxor(s1,s2):
    return ''.join(chr(ord(a) ^ ord(b)) for a,b in zip(s1,s2))

#xor two byte sequences
def xor(b1,b2):
    return bytes([a ^ b for a,b in zip(b1,b2)])

#msg which needs to be a multiple of 16 due to CBC
msg = "This is i great example of AES encryption which is one of the most powerful encryption schemes. However, if an attacker has sufficient infos, s/he can break it."

#check for correct length
if len(msg) % 16 is not 0:
    print("msg has to be a multiple of 16")
    exit()

#__main__
encrypted_msg = []  # encrypted msg
IV = IV.encode()  # converts the IV from strings into bytes
for i in range(0, len(msg), 16):
    substring = bytes(msg[i:i+16], "utf-8")
print("encoded IV: ", IV)
print("substring: ", substring)

#xor two byte sequences
tmp = xor(substring, IV)
print("xor, substring and IV: ", tmp)

#encrypt the block
enc_block = encrypt(tmp, KEY)
IV = enc_block
print("enc_block: ", enc_block)
print("IV: ", enc_block)

#given that there are none-printable characters, it needs to be put in hex
tmp = binascii.hexlify(enc_block).decode("utf-8")
encrypted_msg.append(tmp)

#prints the encrypted blocks
for tmp in encrypted_msg:
    print(tmp)


block_text = msg[128:144]

print(block_text.encode("utf-8"))

