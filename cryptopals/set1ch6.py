import binascii
from LetterFrequency import LetterFrequencyLookup

""" Provide helper functions for string manipulation """
class StrFnc:
	
	""" Repeat the provided string len times, truncate if necessary and return string """
	@staticmethod
	def repeat_to_length(string_to_expand, length):
		return (string_to_expand * ((length/len(string_to_expand))+1))[:length]

	""" Split string and return as an array """	
	@staticmethod
	def split(raw,blocksize):
		return ','.join(raw[i: i+blocksize] for i in range(0, len(raw), blocksize)).split(',')
	
	""" Compute the hamming distance between two hex strings """
	@staticmethod
	def get_hamming_distance(hex1, hex2):
		h1 = StrFnc.split(( bin(int(hex1, 16))[2:] ).zfill(len(hex1) * 4),1)
		h2 = StrFnc.split(( bin(int(hex2, 16))[2:] ).zfill(len(hex2) * 4),1)
		hamming_distance = reduce(lambda bit1, bit2: bit1 + bit2, map(lambda bit1, bit2: int(bit1) ^ int(bit2), h1, h2))
		return hamming_distance / float(len(hex1))	

""" Break repeating XOR """
class FindKeySize:
	def __init__(self):

		f = open("resources/set1ch6.txt",'r')
		content = f.read()

		""" Split ciphertext in keysize blocks and calculate hamming distance on the first and second blocks
			A keysize of 4 refers to 4 characters in the hex string, they actual key size is
			hex values, so that would be 2 hex numbers for example 1d42
		"""
		for keysize in range(4,80,2): 
			hexlified_cipher = StrFnc.split(binascii.hexlify(binascii.a2b_base64(content)),keysize)
			hamming_distance = StrFnc.get_hamming_distance(hexlified_cipher[0],hexlified_cipher[1])
			print "%s\t\tkeysize:%s" % (str(hamming_distance), str(keysize/2))
			
		#hamming_distance = strfnc.get_hamming_distance('this is a test'.encode('hex'),'wokka wokka!!!'.encode('hex'))
		#print hamming_distance	


class FindKey:
	def __init__(self,keysize):
		f = open("resources/set1ch6.txt",'r')
		content = f.read()

		""" Split the ciphtext in keysize blocks """
		hex_blocks = StrFnc.split(binascii.hexlify(binascii.a2b_base64(content)),keysize*2)
		truncated_hex_blocks = hex_blocks[:len(hex_blocks)-1] 
		# we find that the text is not divisible by 5, which makes sense... why wouldn't it! It is a repeating passphrase ICE ICE ICE IC
		# get the first block of each block and put that into an array - we will have 5 arrays in the end
		arr = map(lambda x: StrFnc.split(x,2), truncated_hex_blocks)
		
		for a in range(0,keysize):
			block = [byte[a] for byte in arr]
			SingleByteXORCipher(a,block)
			# now we need to iterate over each blook

class SingleByteXORCipher:
		def __init__(self,a,block):
			ltrfrq = LetterFrequencyLookup()
			for c in range(32,127):
				weight = 0
				xoredResult = "";
				result = {}
				for value in block:
					xoredHexVal = hex(int(value, 16) ^ int(hex(c)[2:], 16))[2:].zfill(2)
					# now we have a hex value
					#print xoredHexVal
					#now make the hex into decimal and turn that into ascii character
					char = xoredHexVal.decode('hex')
					# calculate the total of percentages to get a simplistic weight measure.
					weight = weight + ltrfrq.get(char) / len(block)
					#store the result
					result[char] = weight 
			print "BLOCK " + str(a)
			print max(result, key=result.get)

					

#findSize = FindKeySize()
findKey = FindKey(5)
# looks like the key size is 5, because that was the shortest hamming distance.





