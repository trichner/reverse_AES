from Crypto.Cipher import AES
import binascii
import sys

def decrypt(message, key, iv):
    aes = AES.new(key, AES.MODE_CBC, iv)
    return aes.decrypt(message)

def encrypt(message, key, iv):
    aes = AES.new(key, AES.MODE_CBC, iv)
    return aes.encrypt(message)

ciphertext_hexstr_last = "5cab40d9b7242024d2206cc4e9e09f81"
key = "A9sDFua8sdfI112x"
msg = "This is a great example of AES encryption which is one of the most powerful encryption schemes. However, if an attacker has sufficient infos, s/he can break it."

# we need to work with bytes, let's decode the hexstring
ciphertext_bin_last = binascii.unhexlify(ciphertext_hexstr_last)

# we are using UTF-8, not every character might be 1-byte
msg_bin = bytes(msg, "utf-8")

# split the message in 16 byte blocks
msg_bin_parts = []
for i in range(0, len(msg_bin), 16):
    msg_bin_parts.append(msg_bin[i:i + 16])

# here we do the magic
# we decrypt a single block and provide the message as the 'IV', that results in the actual IV that was used
# for said block
# this works because XOR is a commutative operation
for msg_bin_part in reversed(msg_bin_parts):
    iv = decrypt(ciphertext_bin_last, key, msg_bin_part)
    ciphertext_bin_last = iv

# print the found IV in all its glory
print("The IV in all its glory:")
print("in hex:   '{}'".format(binascii.hexlify(ciphertext_bin_last).decode("utf-8")))
print("in utf-8: '{}'".format(ciphertext_bin_last.decode("utf-8")))
print()

# verify the found IV
ciphertext = encrypt(bytes(msg, "utf-8"), key, ciphertext_bin_last)

print("encrypted message:")

ciphertext_hexstr = binascii.hexlify(ciphertext).decode("utf-8")

for i in range(0, len(ciphertext_hexstr), 32):
    print(ciphertext_hexstr[i:i+32])

is_iv_correct = ciphertext_hexstr_last == ciphertext_hexstr[-32:]

print("our IV is " + "CORRECT" if is_iv_correct else "WRONG")
