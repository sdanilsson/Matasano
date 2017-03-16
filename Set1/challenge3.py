# Cryptopals challenges set 1
# Single-byte XOR cipher 

import sys
import binascii
from Helpers import FrequencyScore

def xor_it(hexmessage):
	# split hexmessage
	splithexstr = ','.join(hexmessage[i: i+2] for i in range(0, len(hexmessage), 2)).split(',')
	xored_dict = {}
	for c in range(65,123):
		# xor each hexvalue with characters A-Z
		xored=[]
		for value in splithexstr:
			x = hex(int(value, 16) ^ int(hex(c), 16))
			# make the xored valye to decimal, then into a character and append to the list.
			xored.append(chr(int(x,16)))	
		xored_dict[chr(c)] = ''.join(xored)
	return xored_dict	
	
if __name__ == "__main__":
	result = xor_it('1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736')
	for key in result:
		if FrequencyScore.englishFreqMatchScore(result[key]) > 2:
			print key,result[key]