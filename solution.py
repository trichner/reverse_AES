from Crypto.Cipher import AES

key = "A9sDFua8sdfI112x"
last_CT = "5cab40d9b7242024d2206cc4e9e09f81"
last_block_text = "he can break it." #block 10
#there are 10 blocks with each 16 characters (including spaces)
msg = "This is i great example of AES encryption which is one of the most powerful encryption schemes. However, if an attacker has sufficient infos, s/he can break it."

#workaround zero_IV
zero_iv = ''.join([chr(0) for i in range(16)])
#does the magic, INPUT=last_CT, MAGIC=decryption with the given KEY, OUTPUT= decrypted msg
def decrypt_last_CT(message, key_):
    aes = AES.new(key_, AES.MODE_CBC, zero_iv)
    return aes.decrypt_last_CT(message)

#take block_cipher_decrypted and XOR it with last_block_text which gives the cipher_text of the second last or 9th block. YAAAY
block_cipher_decrypted = decrypt_last_CT(last_CT, key)
#but in order to XOR I need Binary
block_cipher_encoded = block_cipher_decrypted.encode()
last_block_text_encoded = last_block_text.encode()
#now that I have binary I can reverse XOR to get the output of the 2nd last block, block 9
def xor(b1, b2):
    return bytes([a ^ b for a, b in zip(b1, b2)])
CT_block9 = xor(block_cipher_encoded, last_block_text_encoded)

#now the fun starts, do the same process until the first block
#main TODO ----> need to iterate here but not sure how
for x in range(9): #do this 9 times and the return the IV (CT_block_new of block 1)
    CT_blocks = []
    #decode
    CT_block_new_decoded = CT_block_new.decode()
    #decrypt with key and previous CTs
    block_cipher_text_new = decrypt_last_CT(CT_block_new_decoded, key)
    #make binary to XOR it
    bct_encoded= block_cipher_text_new.encode()
    #find out the current block_text TODO
    for i in msg: #TODO
        start = len(msg) - len(16) #start from here writing down the characters
        for char in start:
            block_text = msg[128:144] #this needs to be adjustable: for every iteration I go 128 - 16 and 144 - 16
    ...
    return block_text
    #enocde it to binary to XOR it
    bt_encoded = block_text.encode()
    #XOR block_cipher_text_new
    CT_block_new = xor(bct_encoded, bt_encoded)
    return CT_block_new
    CT_blocks.append(CT_block_new)

#TODO
for CT_block_new in CT_blocks:
    print(CT_block_new)




