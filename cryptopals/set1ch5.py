import binascii

""" Provide helper functions for string manipulation """
class StrFnc:
	""" Repeat the provided string len times, truncate if necessary and return string """
	def repeat_to_length(self, string_to_expand, length):
		return (string_to_expand * ((length/len(string_to_expand))+1))[:length]
	""" Split string and return as an array """	
	def hex_split(self,raw):
		return ','.join(raw[i: i+2] for i in range(0, len(raw), 2)).split(',')

""" Encode string using repeating XOR """
class Encode:
	""" Encrypt provided file with provided key """
	def encrypt(self, key, filename):
		strfnc = StrFnc()

		f = open(filename,'r')
		content = f.read()

		hex_content = strfnc.hex_split(content.encode('hex'))
		hex_rep_key = strfnc.hex_split(strfnc.repeat_to_length(key.encode('hex'),len(content.encode('hex'))))

		encrypted = ''.join(map(lambda content,key: hex(int(content,16) ^ int(key,16))[2:].zfill(2), hex_content, hex_rep_key))
		
		
		""" test """
		#filename = 'resources/stanza.txt'
		#expected_result = '0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f'	
		#assert(output == expected_result),'Sad Trombone'

		print encrypted

""" Decode string encoded with repeating XOR """
class Decode:
	""" Decrypt provided file with provided key """
	def decode(self, key, filename):
		strfnc = StrFnc()

		f = open(filename,'r')
		content = f.read()
		
		hex_content = strfnc.hex_split(content)
		hex_rep_key = strfnc.hex_split(strfnc.repeat_to_length(key.encode('hex'),len(content)))
		
		decrypted = map(lambda content,key: hex(int(content,16) ^ int(key,16))[2:].zfill(2), hex_content, hex_rep_key)
		clear_text = ''.join(map(lambda hex_num: hex_num.decode('hex'), decrypted))
		
		print clear_text
		
enc = Encode()
enc.encrypt("The long walk home","resources/article.txt")

# dec = Decode()
# dec.decode("The long walk home","resources/article_encoded.txt")

