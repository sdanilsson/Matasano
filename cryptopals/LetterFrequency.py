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