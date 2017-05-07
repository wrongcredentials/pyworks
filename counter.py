symbols = {}

def counter(input):
	for i in input.split():	
		if i not in symbols:
			symbols[i] = 1
		else:
			symbols[i] += 1 
	print(symbols)

counter(input("""
Введите последовательность символов, разделив пробелом.
Например, '1 1 2 3 3 1 10 5'
>>> """))

