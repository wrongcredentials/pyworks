#Python Homework 1

#Задание №1
#Вывести массив вида [3,7,11,...,23] - от 3 до 23 с шагом 4 при помощи функции range 

def task1():
	print("\n    Массив чисел от 3 до 23 с шагом 4:", (list(range(3, 24, 4))))
     
task1()

#Задание №2
#Написать случайный массив чисел из 10-ти элементов. При помощи циклов и условий 
#найти (и вывести) в нем максимальный и минимальный элементы (функциями max и min пользоваться запрещено)

def task2():
	a = [0, 5, 12, 48, -8, 10, 1, -2, 6, 6]	
	minimum = a[0]
	maximum = a[0]
	
	for current_number in a[1:]:
		if (current_number > maximum):
			maximum = current_number	
		
		if (current_number < minimum):
			minimum = current_number

	result = """
    Заданный массив: {}
    Максимальный элемент: {}
    Минимальный элемент: {}
	""".format(a, maximum, minimum)
	print(result)

task2()

#Задание №3
#Написать программу, печатающую на экране первые 10-ть чисел Фибоначчи

def task3():
	a = [0, 1]
	for i in range(8): # 0, 1, 2, 3, 4, 5, 6, 7
		element = a[i] + a[i+1]
		a.append(element)
	
	result = """
    Первые 10 чисел Фибоначчи: {}
	""".format(a)
	print(result)

task3()