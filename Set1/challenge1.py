# Cryptopals challenges set 1
# Convert to base64

import binascii

h='49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
# decodes the string using the codec registered for encoding
hex = h.decode('hex')
print hex
# convert a binary string to base64 
base = binascii.b2a_base64(hex)
print base.rstrip()