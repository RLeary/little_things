def dec_to_bin(number):
	return "{0:b}".format(number)
	
def dec_to_hex(number):
	return "{0:x}".format(number)
	
def dec_to_oct(number):
	return "{0:o}".format(number)
	
# Quick and dirty for next 2 - change later
def bin_to_dec(number):
	return int(number, 2)
	
def bin_to_hex(number):
	return hex(bin_to_dec(number))
	
	