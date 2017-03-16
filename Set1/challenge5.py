# Cryptopals challenges set 1
# Implement repeating-key XOR

import sys
import binascii
from Helpers import FrequencyScore


def repeat_xor_it(key, message):
    # make the key the same length as the string we want to encrypt
    expanded_key = repeat_to_length(key, len(message))

    # split message into char list
    splitmsg = list(message)
    # transform the chars to hex values
    hexmessage = map(lambda x: hex(ord(x)), splitmsg)

    # split the expanded key to char list
    splitkey = list(expanded_key)
    # transform the chars to hex values
    hexkey = map(lambda x: hex(ord(x)), splitkey)

    # xor the message using the key
    encrypted = map(lambda msg, key: hex(int(msg, 16) ^ int(key, 16)).lstrip("0x").zfill(2), hexmessage, hexkey)
    return ''.join(encrypted)


def repeat_to_length(string_to_expand, length):
    return (string_to_expand * ((length / len(string_to_expand)) + 1))[:length]


def decrypt_repeated_xor_string(key, hex_message):
    # split hexed message
    hex_list = [hex_message[i:i + 2] for i in range(0, len(hex_message),2)]
    print hex_list

    expanded_key = repeat_to_length(key, len(hex_list))

    temp_key = list(expanded_key)
    hex_key = map(lambda c: binascii.hexlify(c), temp_key )
    print hex_key

    tuples = zip(hex_list,hex_key)
    print tuples

    result = "".join(map(lambda t: chr(int(t[0],16) ^ int(t[1],16)), tuples))
    print result

if __name__ == "__main__":
    input_file = open('Resources/ch5.txt')
    contents = input_file.read()
    result = repeat_xor_it('few', "fuse fuel for falling flocks")
    print result
    # make it base64
    hex = result.decode("hex")
    base = binascii.b2a_base64(hex)
    print base

    #decrypt_repeated_xor_string('ICE','0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f')
