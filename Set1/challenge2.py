# Cryptopals challenges set 1
# Fixed XOR
import binascii
from Crypto.Util.strxor import strxor

def fixedXor(s):
	h = s.decode('hex')
	key = '686974207468652062756c6c277320657965'	
	#Return the binary data represented by the hexadecimal string hexstr
	bin1 = binascii.unhexlify(s)
	bin2 = binascii.unhexlify(key)
	print "key: "+bin2
	xored = strxor(bin1,bin2)
	print "xored result: "+xored
	#Return make the xored result into a hex string
	return binascii.hexlify(xored)

if __name__ == "__main__":
	result = fixedXor('1c0111001f010100061a024b53535009181c')
	print "the hexed result:"+result
