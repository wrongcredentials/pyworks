#Python Homework 2

#Задание №1 
#Написать функцию, которая на вход принимает список элементов и выводит словарь 
#из того, какой элемент сколько раз встречался (например, "1": "3", "2": "2")

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

#Задание №2
#Написать функцию транслитерации, которая на вход получает строку (в т.ч. с пробелами),
#заменяет буквы (Вася -> Vasya) и на выход отдает измененную строку

from rus_to_eng import dictionary

def transliterator(input):
	output = []
	for i in input:
		if i in dictionary:
			i = dictionary[i]
		output.append(i)	
	print("Транслитерированное выражение: " + "".join(output))

transliterator(input("Введите текст для транслитерации: "))
