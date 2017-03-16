import binascii
import re
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
					# now we have the xored hex value
					#print xoredHexVal
					#now make the hex into decimal and turn that into ascii character
					char = xoredHexVal.decode('hex')
					# calculate the total of percentages to get a simplistic weight measure.
					weight = weight + ltrfrq.get(char) / len(h)
					xoredResult = xoredResult + char
				#print xoredResult + ' ' + str(weight)
				#if weight > 1.6 and weight < 1.7:
				#	print xoredResult + ' ' + str(weight)
				if re.search('\A[A-Z][a-z]{2} .*',xoredResult):
					print "["+ xoredResult + "] " + str(weight) 1+ "using char ["+char+"]"



sbxorc = SingleByteXORCipher()
lines = [line.rstrip('\n') for line in open('4.txt')]
# single byte xor cipher
for l in lines:
	sbxorc.decrypt(l)