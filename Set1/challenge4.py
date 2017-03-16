# Cryptopals challenges set 1
# Single-byte XOR cipher 

import sys
import binascii
from Crypto.Util.strxor import strxor
from Helpers import FrequencyScore

def xor_it(hexmessage):
	# split hexmessage
	splithexstr = ','.join(hexmessage[i: i+2] for i in range(0, len(hexmessage), 2)).split(',')
	xored_dict = {}
	# In order to ferret out the right key I had to increase the range of ascii to compare with.
	for c in range(32,127):
		# xor each hexvalue with characters A-Z
		xored=[]
		for value in splithexstr:
			x = hex(int(value, 16) ^ int(hex(c), 16))
			# make the xored valye to decimal, then into a character and append to the list.
			xored.append(chr(int(x,16)))	
		xored_dict[chr(c)] = ''.join(xored)
	return xored_dict	
	
if __name__ == "__main__":
	
	lines = [line.rstrip('\n') for line in open('Resources/ch4.txt')]
	for l in lines:
		result = xor_it(l)
		for key in result:
			if FrequencyScore.englishFreqMatchScore(result[key]) >= 5:
				print key,result[key]	