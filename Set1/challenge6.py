# Cryptopals challenges set 1
# Break repeating-key XOR - find the key that was used to encrypt the message

import binascii
from Helpers import LetterFrequency
from Helpers import FrequencyScore
from operator import itemgetter
import operator
from Helpers import NAvgHD


def base64toBytes(message):
    return binascii.a2b_base64(message)


def bytesToHex(message):
    return binascii.b2a_hex(message).decode()


def split_text(binaryTxt):
    splitmsg = list(binaryTxt)
    return splitmsg


# input: string1, string2
def calculate_hamming_dist_test(h1, h2):
    # split strings to characters
    splittxt1 = split_text(h1)
    splittxt2 = split_text(h2)
    # convert characters to binary string representation
    hex1 = map(lambda x: bin(int(hex(ord(x)), 16)).lstrip("0b").zfill(8), splittxt1)
    hex2 = map(lambda x: bin(int(hex(ord(x)), 16)).lstrip("0b").zfill(8), splittxt2)

    # create tuples
    zipped = zip(hex1, hex2)

    # calculate the hamming distance
    distance = 0
    for tuple in zipped:
        distance = distance + sum(c1 != c2 for c1, c2 in zip(tuple[0], tuple[1]))

    return distance


def get_key_size(source):

    # THIS IS IMPORTANT, READ THIS TO UNDERSTAND HOW TO ACTUALLY GET THE SIZE OF THE KEY. I think I have been doing this wrong all along.

    # split source to an array of hex numbers.
    hex_list = [int(str(source[i:i + 2]), 16) for i in range(0, len(source), 2)]
    # convert hex characters to binary string representation
    bin_list = map(lambda x: bin(x).lstrip("0b").zfill(8), hex_list)

    #ks = 2
    #for ks in range(2, len(bin_list)/2):
    d = {}
    for ks in range(2, 40):
        #d[ks] = NAvgHD.getNormalizedHammingDistance(ks, bin_list)
        print str(ks)+ ' ' + str(NAvgHD.getNormalizedHammingDistance(ks, bin_list))

    print sorted(d.items(), key=lambda x: x[1], reverse=True)

def find_key(key_size, source):
    print 'Split the hex string into ' + str(key_size) + ' blocks'
    hex_list = [int(str(source[i:i + 2]), 16) for i in range(0, len(source), 2)]
    print hex_list
    # zip the list into key sized chunks
    chunks = zip(*[iter(hex_list)] * key_size)
    # transpose the chunks
    transposed = zip(*chunks)
    # now we need to solve for single xor
    for chunk in transposed:
        get_english_histogram(chunk, key_size)


def get_english_histogram(byteChunk, key_size):
    d = {}
    for c in range(32, 127):
        # xor each hexvalue with characters A-Z
        score = 0;
        for value in byteChunk:
            xored_val = value ^ c
            # score = score + LetterFrequency.getLetterFrequency(chr(xored_val))
            # need to filter out anything that looks like punctuation and blankspace
            score = score + FrequencyScore.englishFreqMatchScore(chr(xored_val))
            d[chr(c)] = score / key_size
        # print chr(c) + " " +str(score)
    print sorted(d.items(), key=lambda x: x[1], reverse=True)


def decrypt_repeated_xor_string(key, hex_message):
    # split hexed message
    hex_list = [hex_message[i:i + 2] for i in range(0, len(hex_message), 2)]
    expanded_key = repeat_to_length(key, len(hex_list))
    temp_key = list(expanded_key)
    hex_key = map(lambda c: binascii.hexlify(c), temp_key)
    tuples = zip(hex_list, hex_key)
    result = "".join(map(lambda t: chr(int(t[0], 16) ^ int(t[1], 16)), tuples))
    print result


def repeat_to_length(string_to_expand, length):
    return (string_to_expand * ((length / len(string_to_expand)) + 1))[:length]


if __name__ == "__main__":
    input_file = open('Resources/ch6.txt')
    # input_file = open('Resources/smartcookieB64.txt')
    #input_file = open('Resources/ch5b64_ICE.txt')
    #input_file = open('Resources/fusefuel.txt')
    contents = input_file.read()
    bytes = base64toBytes(contents)
    hexstring = bytesToHex(bytes)
    # The key size seems to be 5, the difference is only 1.2 compared to 2.5+ for everything else
    #get_key_size(hexstring)
    # candidates 7, 9, 11,
    #find_key(3,hexstring)
    #decrypt_repeated_xor_string('Terminator X: Bring the noise',hexstring)
