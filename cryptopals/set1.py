__author__ = 'nilssona'

import binascii

class Conversions:
	def hex2Base64(self,h):
		hex = h.decode('hex');
		return binascii.b2a_base64(hex).strip() 		

	def fixedXor(self,s1,s2):
		# This challenge is worded in a misleading way.
		# To clarify: The goal is to xor the two hex strings. 
		# Make the strings into a hex strings, then xor, then splice to remove the 0x and the L for long, then return
		# The int(s1,16) is to specify the base. Hex in this case.
		return hex(int(s1, 16) ^ int(s2, 16))[2:len(s1)]
		

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
				if weight > 2 and weight < 2.8:
					print xoredResult + ' ' + str(weight)	

class LetterFrequencyLookup:
	def get(self,ltr):
		frequency = {}
		frequency['a'] = 8.167
		frequency['b'] = 1.492
		frequency['c'] = 2.782
		frequency['d'] = 4.253
		frequency['e'] = 12.702
		frequency['f'] = 2.228
		frequency['g'] = 2.015
		frequency['h'] = 6.094
		frequency['i'] = 6.966
		frequency['j'] = 0.153
		frequency['k'] = 0.772
		frequency['l'] = 4.025
		frequency['m'] = 2.406
		frequency['n'] = 6.749
		frequency['o'] = 7.507
		frequency['p'] = 1.929
		frequency['q'] = 0.095
		frequency['r'] = 5.987
		frequency['s'] = 6.327
		frequency['t'] = 9.056
		frequency['u'] = 2.758
		frequency['v'] = 0.978
		frequency['w'] = 2.361
		frequency['x'] = 0.150
		frequency['y'] = 1.974
		frequency['z'] = 0.074
		frequency['A'] = 8.167
		frequency['B'] = 1.492
		frequency['C'] = 2.782
		frequency['D'] = 4.253
		frequency['E'] = 12.702
		frequency['F'] = 2.228
		frequency['G'] = 2.015
		frequency['H'] = 6.094
		frequency['I'] = 6.966
		frequency['J'] = 0.153
		frequency['K'] = 0.772
		frequency['L'] = 4.025
		frequency['M'] = 2.406
		frequency['N'] = 6.749
		frequency['O'] = 7.507
		frequency['P'] = 1.929
		frequency['Q'] = 0.095
		frequency['R'] = 5.987
		frequency['S'] = 6.327
		frequency['T'] = 9.056
		frequency['U'] = 2.758
		frequency['V'] = 0.978
		frequency['W'] = 2.361
		frequency['X'] = 0.150
		frequency['Y'] = 1.974
		frequency['Z'] = 0.074

		if ltr in frequency:
			return frequency[ltr];
		else:
			return 0;

#test = Conversions()
#sbxorc = SingleByteXORCipher()
#fr = LetterFrequencyLookup()

# # hex to base64
# result = test.hex2Base64("49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d")
# expected_result1 = "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"
# print result
# assert(result == expected_result1),"Conversion failed"


# # fixed xor test
 xorRes = test.fixedXor('1c0111001f010100061a024b53535009181c','686974207468652062756c6c277320657965')
 #expected_result2 = '746865206b696420646f6e277420706c6179'
 #assert(xorRes == expected_result2),"Failed"
 print xorRes

# https://jeffknupp.com/blog/2013/04/07/improve-your-python-yield-and-generators-explained/
# single byte xor cipher
sbxorc.decrypt('1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736')



