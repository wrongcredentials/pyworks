def file():
	f = open("test.txt", "r", encoding = "utf-8")
	print(f.readline())
	print(f.readline())
	f.seek(0, 0) #указатель, 1 - куда, 2 - откуда
	#print(f.readlines())
	print(f.read())
	f.close()

	f2 = open("wt.txt", "w+")
	f2.write("Test\nTest2\nTest3")
	f2.close()

	with open("wt2.txt", "w+") as f3:
		f3.write("Test")

import json
def json1():
	#json here
	with open("data.json", "w+") as f:
		json.dump(obj, f)

	with open("data.json", "r") as f:
		json.load(f)

import sys
print(sys.argv)

#TODO List
#python todo.py
List
Add "Uptime"
Remove 1
Up 3
Down 2
