def bin_reader(string):
	"""reads long strings of binary"""
	def binary(string):
		tot = 0
		for i in range(0,8):
			if (string[i:(i+1)] == "1"):	tot += 2**(7-i)
		return chr(tot)
	
	def breaker(string,num):
		liz = []
		for i in range(0,len(string),num):	liz.append(string[i:(i+num)])
		return liz
	
	var,mess = breaker(string,8), ''
	for i in range(0,len(var)):	mess += binary(var[i])
	return mess

def gener_bin(message):
	"""writes a binary string out of a normal string"""
	mess = ''
	for i in range(0,len(message)):
		num = ord(message[i:(i+1)])
		for j in range(0,8):
			if ((num - (2**(7-j))) >= 0):
				mess += "1"
				num -= (2**(7-j))
			else:	mess += "0"
	return mess
