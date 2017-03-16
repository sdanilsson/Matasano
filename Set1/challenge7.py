import base64
from Crypto.Cipher import AES

# def decryptAES(msg,key):
#     cryptbytes = base64.b64decode(msg)
#     text = Crypto.Cipher.decrypt_aes_ecb(cryptbytes, key).decode()
#    print text

# def decrypt(encrypted, passphrase):
#     message_bytes = base64.b64decode(msg)
#     aes = Crypto.Cipher.AES.new(passphrase,AES.MODE_CFB,)
#     IV = Random.new().read(BLOCK_SIZE)
#     aes = AES.new(passphrase, AES.MODE_CFB, IV)
#     return aes.decrypt(base64.b64decode(encrypted))


# Decryption
def decryptAES(message,passphrase):
    print passphrase
    decryption_suite = AES.new()
    plain_text = decryption_suite.decrypt(message)
    #print plain_text

if __name__ == "__main__":
    input_file = open('Resources/ch7.txt')
    contents = input_file.read()
    decryptAES(base64.b64decode(contents),b'YELLOW SUBMARINE')

from Crypto.Cipher import AES
# Encryption
#encryption_suite = AES.new('This is a key123', AES.MODE_CBC, 'This is an IV456')
#cipher_text = encryption_suite.encrypt("A really secret message. Not for prying eyes.")
