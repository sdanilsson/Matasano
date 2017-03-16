__author__ = 'nilssona'

import binascii
from LetterFrequency import LetterFrequencyLookup

class SingleByteXORCipher:
		def decrypt(self,h):
			ltrfrq = LetterFrequencyLookup()
			splitStr = ','.join(h[i: i+2] for i in range(0, len(h), 2)).split(',')
			for c in range(32,127):
				weight = 0
				xoredResult = "";
				for value in splitStr:
					xoredHexVal = hex(int(value, 16) ^ int(hex(c)[2:], 16))[2:].zfill(2)
					# now we have a hex value
					#print xoredHexVal
					#now make the hex into decimal and turn that into ascii character
					char = xoredHexVal.decode('hex')
					# calculate the total of percentages to get a simplistic weight measure.
					weight = weight + ltrfrq.get(char) / len(h)
					xoredResult = xoredResult + char	
				#print xoredResult + ' ' + str(weight)
				if weight > 2.0 and weight < 2.1:
					print xoredResult + ' ' + str(weight)



sbxorc = SingleByteXORCipher()
# single byte xor cipher
sbxorc.decrypt('1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736')
