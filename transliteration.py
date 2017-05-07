from rus_to_eng import dictionary

def transliterator(input):
	output = []
	for i in input:
		if i in dictionary:
			i = dictionary[i]
		output.append(i)	
	print("Транслитерированное выражение: " + "".join(output))

transliterator(input("Введите текст для транслитерации: "))
